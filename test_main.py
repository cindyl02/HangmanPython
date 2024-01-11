import main
from hangman_art import stages


def test_hangman_win(capfd, monkeypatch):
    inputs = ["h", "a", "n", "g", "m", "a", "n"]
    monkeypatch.setattr("main.get_word", lambda: "hangman")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "The answer is hangman. You lose." not in out
    assert "You lose a life" not in out
    assert "You've already guessed" not in out
    assert "h _ _ _ _ _ _" in out
    assert "h a _ _ _ a _" in out
    assert "h a n _ _ a n" in out
    assert "h a n g _ a n" in out
    assert "h a n g m a n" in out
    assert "h a n g m a n" in out
    assert f"You win.\n{stages[6]}" in out

    for i in range(6):
        assert stages[i] not in out


def test_hangman_lose_all_lives(capfd, monkeypatch):
    inputs = ["c", "d", "e", "f", "l", "i"]
    monkeypatch.setattr("main.get_word", lambda: "hangman")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "You win.\n" not in out
    assert "You've already guessed" not in out
    assert "The answer is hangman. You lose." in out
    assert "_ _ _ _ _ _ _" in out
    assert stages[6] not in out

    for i in range(6):
        assert stages[i] in out
    for guess in inputs:
        assert f"You guessed {guess} which is not in the word. You lose a life" in out


def test_hangman_bad_guess_lose_all_lives_but_one(capfd, monkeypatch):
    inputs = ["aa", "d", "e", "l", "m", "c", "a", "t"]
    monkeypatch.setattr("main.get_word", lambda: "cat")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "The answer is cat. You lose." not in out
    assert "You've already guessed" not in out
    assert "_ _ _" in out
    assert "c _ _" in out
    assert "c a _" in out
    assert "c a t" in out
    assert f"You win.\n{stages[1]}" in out
    assert stages[6] not in out
    assert stages[0] not in out

    for i in range(1, 6):
        assert stages[i] in out

    for guess in inputs:
        if guess not in "cat":
            assert f"You guessed {guess} which is not in the word. You lose a life" in out


def test_hangman_bad_guess_lose_one_life(capfd, monkeypatch):
    inputs = ["m", "c", "a", "t"]
    monkeypatch.setattr("main.get_word", lambda: "cat")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "The answer is cat. You lose." not in out
    assert "You guessed m which is not in the word. You lose a life" in out
    assert "You've already guessed" not in out
    assert "_ _ _" in out
    assert "c _ _" in out
    assert "c a _" in out
    assert "c a t" in out
    assert f"You win.\n{stages[5]}" in out
    assert stages[6] not in out

    for i in range(5):
        assert stages[i] not in out


def test_hangman_bad_guess_lose_three_lives(capfd, monkeypatch):
    inputs = ["d", "e", "l", "c", "a", "t"]
    monkeypatch.setattr("main.get_word", lambda: "cat")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "The answer is cat. You lose." not in out
    assert "You've already guessed" not in out
    assert "_ _ _" in out
    assert "c _ _" in out
    assert "c a _" in out
    assert "c a t" in out
    assert f"You win.\n{stages[3]}" in out

    for i in range(7):
        if i < 3 or i == 6:
            assert stages[i] not in out
        else:
            assert stages[i] in out

    for guess in inputs:
        if guess not in "cat":
            assert f"You guessed {guess} which is not in the word. You lose a life" in out


def test_hangman_already_guessed(capfd, monkeypatch):
    inputs = ["c", "c", "a", "t"]
    monkeypatch.setattr("main.get_word", lambda: "cat")
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.hangman()
    out, err = capfd.readouterr()

    assert "c a t" in out
    assert f"You win.\n{stages[6]}" in out
    assert "The answer is cat. You lose." not in out
    assert "You lose a life" not in out
    assert "You've already guessed c" in out

    for i in range(6):
        assert stages[i] not in out
