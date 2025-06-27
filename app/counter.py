from nicegui import ui

def create():
    @ui.page('/')
    def page():
        # Initialize counter value
        count = 0
        
        # Create label to display the count
        count_label = ui.label(f'Count: {count}')
        
        # Function to increment the counter
        def increment():
            nonlocal count
            count += 1
            count_label.set_text(f'Count: {count}')
        
        # Create increment button
        ui.button('Increment', on_click=increment)