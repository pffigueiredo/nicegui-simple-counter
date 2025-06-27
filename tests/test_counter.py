from nicegui.testing import User
from nicegui import ui

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    await user.should_see('Count: 0')

async def test_counter_increment(user: User) -> None:
    """Test that clicking increment button increases the count"""
    await user.open('/')
    
    # Initial state
    await user.should_see('Count: 0')
    
    # Click increment button once
    user.find('Increment').click()
    await user.should_see('Count: 1')
    
    # Click increment button again
    user.find('Increment').click()
    await user.should_see('Count: 2')
    
    # Click multiple times
    for i in range(3, 8):
        user.find('Increment').click()
        await user.should_see(f'Count: {i}')

async def test_counter_button_exists(user: User) -> None:
    """Test that increment button is present"""
    await user.open('/')
    # Check that we can find the increment button
    button = user.find('Increment')
    assert button.elements, "Increment button should exist"

async def test_counter_label_exists(user: User) -> None:
    """Test that count label is present"""
    await user.open('/')
    await user.should_see('Count: 0')