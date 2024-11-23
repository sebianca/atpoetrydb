import requests


def test_get_poem_by_title():
    # Step 1: Send GET request
    response = requests.get("https://poetrydb.org/title/Ozymandias")

    # Step 2: Test status code is 200 and parse JSON response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    poems = response.json()

    # Step 3: Verify that a poem is returned
    assert len(poems) > 0, "No poems found in the response"

    poem = poems[0]  # Get the first poem
    # Step 4: Verify poem title
    assert poem["title"] == "Ozymandias", f"Expected title 'Ozymandias', got {poem['title']}"
    # Step 5: Verify poem author
    assert poem["author"] == "Percy Bysshe Shelley", f"Expected author 'Percy Bysshe Shelley', got {poem['author']}"

    # Step 6: Verify line count is 14
    assert poem["linecount"] == "14", f"Expected linecount '14', got {poem['linecount']}"
    # Step 7: Verify line count is the same as the number of lines returned in res
    assert len(poem["lines"]) == 14, f"Expected 14 lines, got {len(poem['lines'])}"


def test_get_poems_by_author():
    # Step 1: Send GET request
    response = requests.get("https://poetrydb.org/author/Emily Dickinson")

    # Step 2: Parse JSON response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    poems = response.json()

    # Step 3: Verify that one or more poems returned
    assert len(poems) > 0, "No poems found in the response"

    # Step 4: Verify author and line count for each poem
    for poem in poems:
        assert poem["author"] == "Emily Dickinson", f"Expected author 'Emily Dickinson', got {poem['author']}"

        # Verify line count without empty lines used as separators
        not_empty_lines = [line for line in poem['lines'] if line.strip()]
        assert int(poem["linecount"]) == len(not_empty_lines), f"Expected linecount {len(not_empty_lines)}, got {poem['linecount']}"


def test_invalid_endpoint():
    # Step 1: Send GET request to an invalid endpoint
    response = requests.get("https://poetrydb.org/title/404")

    # Step 2: Verify status code is 200, normally it should be 404
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    #Step 3: Verify error message in response
    json_body = response.json()
    assert json_body.get('status') == 404, f"Expected status code 404, got {json_body.get('status')}"
    assert json_body.get('reason') == "Not found", f"Expected reason 'Not Found', got {json_body.get('reason')}"

