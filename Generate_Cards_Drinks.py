import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle
import textwrap

def create_dinner_card(ax, meal, date, location):
    # Add a black border by creating a rectangle that covers the edges of the subplot
    rect = Rectangle((0, 0), 1, 1, linewidth=5, edgecolor='black', facecolor='none', transform=ax.transAxes)
    ax.add_patch(rect)

    # Add date, meal, and location text
    ax.text(0.5, 0.85, date, fontsize=16, weight='bold', ha='center', transform=ax.transAxes)
    
    # Wrap text manually if necessary
    wrapped_meal = textwrap.fill(meal, width=20)  # Adjust 'width' as needed based on your text and font size
    ax.text(0.5, 0.5, wrapped_meal, fontsize=12, ha='center', va='center', transform=ax.transAxes)

    ax.text(0.5, 0.15, location, fontsize=10, ha='center', weight='bold', transform=ax.transAxes)

    # Remove axes
    ax.axis('off')


# Create a PDF to hold the business cards
pdf_pages = PdfPages('drinks_cards.pdf')

# Constants for an A4 page and cards
A4_WIDTH_INCHES = 8.27  # A4 paper width in inches
A4_HEIGHT_INCHES = 11.69  # A4 paper height in inches
CARDS_PER_ROW = 2
ROWS_PER_PAGE = 5
CARDS_PER_PAGE = CARDS_PER_ROW * ROWS_PER_PAGE

# Dictionary of meals and counts (example data)
meals = {
    'Água Refrigerante Limonada': 250,
    }


# Initialize a new A4 page
fig, axs = plt.subplots(ROWS_PER_PAGE, CARDS_PER_ROW, figsize=(A4_WIDTH_INCHES, A4_HEIGHT_INCHES))
card_counter = 0

# Create and add cards to the PDF
for meal, count in meals.items():
    for _ in range(count):
        # Calculate position of the next card
        row = card_counter // CARDS_PER_ROW
        col = card_counter % CARDS_PER_ROW

        # Create the card on the appropriate subplot
        create_dinner_card(axs[row, col], meal, 'Bebidas', 'SW Blumenau')
        card_counter += 1

        # When a page is full or all cards have been created, save the page and start a new one
        if card_counter == CARDS_PER_PAGE or (meal == list(meals.keys())[-1] and count == _ + 1):
            plt.tight_layout()
            pdf_pages.savefig(fig)
            plt.close(fig)
            
            # Reset counter and create a new figure if there are more cards to process
            card_counter = 0
            if meal != list(meals.keys())[-1] or count != _ + 1:
                fig, axs = plt.subplots(ROWS_PER_PAGE, CARDS_PER_ROW, figsize=(A4_WIDTH_INCHES, A4_HEIGHT_INCHES))

# Finalize and close the PDF file
pdf_pages.close()
