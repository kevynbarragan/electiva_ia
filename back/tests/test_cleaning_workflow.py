import pandas as pd
import pytest
from fastapi import HTTPException
from app.main import _apply_selected, recommendations


def test_missing_preview_uses_real_median_and_does_not_mutate_source():
    source = pd.DataFrame({"score": [10.0, None, 30.0]})
    result, summary = _apply_selected(source, "missing", "score", [1], {"method": "median"})
    assert result.loc[1, "score"] == 20.0
    assert pd.isna(source.loc[1, "score"])
    assert summary["cells_changed"] == 1
    assert summary["source_rows"] == summary["result_rows"] == 3


def test_duplicate_removal_only_changes_working_copy():
    source = pd.DataFrame({"x": [1, 1, 2], "category": ["a", "a", "b"]})
    result, summary = _apply_selected(source, "duplicates", "", [0, 1], {"method": "drop_rows"})
    assert len(result) == 2
    assert len(source) == 3
    assert summary["rows_removed"] == 1


def test_outlier_review_does_not_change_values():
    source = pd.DataFrame({"measure": [1, 2, 3, 100]})
    result, summary = _apply_selected(source, "outliers", "measure", [3], {"method": "review", "bounds": "iqr", "factor": 1.5})
    assert result.equals(source)
    assert summary["cells_changed"] == 0
    assert summary["rows_removed"] == 0


def test_rejects_stale_or_non_affected_selection():
    source = pd.DataFrame({"x": [1.0, None, 3.0]})
    with pytest.raises(HTTPException):
        _apply_selected(source, "missing", "x", [0], {"method": "median"})


def test_numeric_category_codes_are_not_recommended_as_iqr_outliers():
    source = pd.DataFrame({"Browser": [1, 2, 2, 12, 2, 2], "amount": [1, 2, 3, 4, 5, 100]})
    ids = [item["id"] for item in recommendations(source)]
    assert not any(item.startswith("outliers:Browser") for item in ids)
