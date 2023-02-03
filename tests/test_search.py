import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page

ANIMALS = [
    'panda',
    'python',
    'polar bear',
    'parrot',
    'porcupine',
    'parakeet',
    'pangolin',
    'panther',
    'platypus',
    'peacock'
]


@pytest.mark.parametrize('phrase', ANIMALS)
def test_basic_duckduckgo_search(
        phrase: str,
        page: Page,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None:
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase)

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase)

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{phrase} at DuckDuckGo')

# --headed --slowmo 100: Basic
# $ python -m pytest tests --browser chromium --browser firefox --browser webkit --verbose (show result separated)
# --screenshot on: Take a screenshot if tests are failed. --output: allocates screenshot file to exact directory.
# Each run clean-out folder for screenshots. --screenshot only-on-failure: use screenshot if fail only
# --video retain-on-failure: Capture video if failed
# python -m pytest tests -n 2: Run two test in parallel
