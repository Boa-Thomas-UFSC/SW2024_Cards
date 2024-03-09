import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle
import textwrap
from matplotlib.font_manager import FontProperties

def create_dinner_card(ax, meal, date, location, font_path):
    # Load the custom font
    custom_font = FontProperties(fname=font_path)
    
    # Add a black border by creating a rectangle that covers the edges of the subplot
    rect = Rectangle((0, 0), 1, 1, linewidth=5, edgecolor='black', facecolor='none', transform=ax.transAxes)
    ax.add_patch(rect)

    # Add date, meal, and location text with the custom font
    ax.text(0.5, 0.85, date, fontsize=16, weight='bold', ha='center', transform=ax.transAxes, fontproperties=custom_font)
    
    # Wrap text manually if necessary
    wrapped_meal = textwrap.fill(meal, width=20)  # Adjust 'width' as needed based on your text and font size
    ax.text(0.5, 0.5, wrapped_meal, fontsize=12, ha='center', va='center', transform=ax.transAxes, fontproperties=custom_font)

    ax.text(0.5, 0.15, location, fontsize=10, ha='center', weight='bold', transform=ax.transAxes, fontproperties=custom_font)

    # Remove axes
    ax.axis('off')

# Path to your custom font
font_path = 'HelveticaNowDisplay-Regular.ttf'  # Replace with the actual path to your .ttf font file

# Create a PDF to hold the business cards
pdf_pages = PdfPages('lunch_cards1003_v2.pdf')

# Constants for an A4 page and cards
A4_WIDTH_INCHES = 8.27  # A4 paper width in inches
A4_HEIGHT_INCHES = 11.69  # A4 paper height in inches
CARDS_PER_ROW = 2
ROWS_PER_PAGE = 5
CARDS_PER_PAGE = CARDS_PER_ROW * ROWS_PER_PAGE

# Dictionary of meals and counts (example data)
#Lunch 09/03
# meals = {
#     'Lanche - Pão carne e queijo': 4,
#     'Lanche - Smaga bacon': 23,  # Combined count for "Smaga bacon (120g de carne, picles de pepino, cebola roxa e bacon) + batata de 60g" and "Smaga Bacon + 60g de batata"
#     'Lanche - Smaga salada': 7,  # Combined count for "Smaga salada (120g de carne com alface e tomate) + batata de 60g" and "Smaga salada + batata de 60g"
#     'Sushi - Combo 15 peças sushi': 30,
#     'Massa - Gnocchi com molho Al Ragú di Carne': 2,
#     'Massa - Gnocchi com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 3,
#     'Massa - Gnocchi com molho Lasagne alla Bolognese': 1,
#     'Massa - Penne com molho Al Sugo': 1,
#     'Massa - Penne com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 2,
#     'Massa - Penne com molho Lasagne alla Bolognese': 2,
#     'Massa - Penne com molho Lasagne di Pollo': 2,
#     'Massa - Spaghetti com molho Al Ragú di Carne': 1,
#     'Massa - Spaghetti com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 2,
#     'Pizza - Calabresa': 9,
#     'Pizza - Margherita': 9,
#     'Pizza - Pepperoni': 2,  # Combined count for "Pepperoni" and the repeated "Pepperoni"
#     'Pizza - Piu Piu': 3
#     }

#Lunch 10/03
meals = {
    'Lanche - Pão carne e queijo': 10,
    'Lanche - Smaga Bacon + 60g de batata': 10,
    'Lanche - Smaga salada + batata de 60g': 10,
    'Sushi - Combo 15 peças sushi': 10,
    'Massa - Gnocchi com molho Lasagne alla Bolognese': 5,
    'Massa - Penne com molho Lasagne alla Bolognese': 5,
    'Massa - Penne com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 10,
    'Massa - Spaghetti com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 10,
    'Massa - Gnocchi com molho Al Ragú di Carne': 10,
    'Massa - Spaghetti com molho Al Sugo': 10,
    'Massa - Penne com molho Al Ragú di Carne': 10,
    'Massa - Spaghetti com molho Lasagne di Pollo': 10,
    'Massa - Penne com molho Lasagne di Pollo': 10,
    'Pizza - Calabresa': 5,
    'Pizza - Margherita': 5,
    'Pizza - Piu Piu': 5,
    'Pizza - Pepperoni': 5,
    'Arroz, feijão, iscas de filé suíno empanado ao molho barbecue, fritas e salada verde': 15,
    'Arroz, feijão, bife grelhado, ovo frito, fritas e salada verde': 15,
    'Massa - Gnocchi com molho Cremoso con Pollo, Salami e Pomodoro Secchi': 10,
    'Massa - Spaghetti com molho Al Ragú di Carne': 10
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
        create_dinner_card(axs[row, col], meal, 'Almoço 10/03', 'SW Blumenau', font_path)
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
