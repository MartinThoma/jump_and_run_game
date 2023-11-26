from jump_and_run_game import Player


def test_player_movements():
    # Arrange
    player = Player(0, 0)

    # Act
    player.move_left()
    player.move_right()

    # Assert
    assert player.x == 0
    assert player.y == 0


def test_player_jump():
    # Arrange
    player = Player(0, 0)
    assert player.is_jumping is False

    # Act
    player.jump()

    # Assert
    assert player.is_jumping is True


def test_player_update():
    player = Player(0, 0)
    player.update()
