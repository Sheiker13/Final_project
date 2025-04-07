
import pytest
from movies.forms import ReviewForm

@pytest.mark.django_db
def test_review_form_valid():
    form_data = {"text": "Amazing movie!"}
    form = ReviewForm(data=form_data)
    assert form.is_valid()
