from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QMenuBar, QFileDialog, QInputDialog, QListView, \
    QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel, QInputDialog, QFileDialog, QWidget

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Recipe:
    def __init__(self, name, ingredients, directions):
        self.name = name
        self.ingredients = ingredients
        self.directions = directions

class RecipesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.recipes = [Recipe("Pop Tarts", [Ingredient("Pop Tart", "1 packet")], "Toast the poptarts ...\nor don't.")]

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        open_action = file_menu.addAction('Open')
        open_action.triggered.connect(self.open_file)

        save_action = file_menu.addAction('Save')
        save_action.triggered.connect(self.save_file)

        exit_action = file_menu.addAction('Exit')
        exit_action.triggered.connect(self.close)

        recipe_menu = menubar.addMenu('Recipe')
        add_action = recipe_menu.addAction('Add')
        add_action.triggered.connect(self.add_recipe)

        remove_action = recipe_menu.addAction('Remove')
        remove_action.triggered.connect(self.remove_recipe)

        layout = QVBoxLayout()

        recipe_list = QListView()
        recipe_list.addItems([recipe.name for recipe in self.recipes])
        recipe_list.clicked.connect(self.select_recipe)

        layout.addWidget(recipe_list)

        ingredients_grid = QVBoxLayout()
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_ingredient)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.remove_ingredient)

        self.ingredients_list = QListView()
        self.ingredient_name_field = QLineEdit()
        self.amount_field = QLineEdit()

        ingredients_grid.addWidget(add_button)
        ingredients_grid.addWidget(remove_button)
        ingredients_grid.addWidget(self.ingredients_list)
        ingredients_grid.addWidget(QLabel("Name:"))
        ingredients_grid.addWidget(self.ingredient_name_field)
        ingredients_grid.addWidget(QLabel("Amount:"))
        ingredients_grid.addWidget(self.amount_field)

        self.ingredients_list.clicked.connect(self.select_ingredient)
        self.ingredient_name_field.textChanged.connect(self.update_selected_ingredient)
        self.amount_field.textChanged.connect(self.update_selected_ingredient)

        layout.addLayout(ingredients_grid)

        directions_area = QTextEdit()
        directions_area.textChanged.connect(self.update_directions)

        layout.addWidget(directions_area)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Recipe File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                self.recipes = []
                num_recipes = int(lines.pop(0).strip())
                for _ in range(num_recipes):
                    name = lines.pop(0).strip()
                    num_ingredients = int(lines.pop(0).strip())
                    ingredients = [Ingredient(lines.pop(0).strip(), lines.pop(0).strip()) for _ in range(num_ingredients)]
                    directions = ""
                    while True:
                        line = lines.pop(0).strip()
                        if line == ".":
                            break
                        directions += line + "\n"
                    self.recipes.append(Recipe(name, ingredients, directions.strip()))

                self.update_recipe_list()

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Recipe File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(f"{len(self.recipes)}\n")
                for recipe in self.recipes:
                    file.write(f"{recipe.name}\n")
                    file.write(f"{len(recipe.ingredients)}\n")
                    for ingredient in recipe.ingredients:
                        file.write(f"{ingredient.name}\n")
                        file.write(f"{ingredient.amount}\n")
                    file.write(recipe.directions + "\n")
                    file.write(".\n")

    def add_recipe(self):
        name, ok = QInputDialog.getText(self, "Recipe Name", "What is the name of the new recipe?")
        if ok:
            new_recipe = Recipe(name, [Ingredient("Stuff", "Some")], "Directions")
            self.recipes.append(new_recipe)
            self.update_recipe_list()
            self.select_recipe()

    def remove_recipe(self):
        selected_index = self.ui.recipe_list.currentIndex().row()
        if selected_index >= 0:
            del self.recipes[selected_index]
            self.update_recipe_list()
            self.select_recipe()

    def add_ingredient(self):
        recipe_index = self.ui.recipe_list.currentIndex().row()
        if recipe_index >= 0:
            new_ingredient = Ingredient("Stuff", "Some")
            self.recipes[recipe_index].ingredients.append(new_ingredient)
            self.update_ingredients_list()

    def remove_ingredient(self):
        recipe_index = self.ui.recipe_list.currentIndex().row()
        ingredient_index = self.ui.ingredients_list.currentIndex().row()
        if recipe_index >= 0 and ingredient_index >= 0:
            del self.recipes[recipe_index].ingredients[ingredient_index]
            self.update_ingredients_list()
            self.update_fields()

    def select_recipe(self):
        selected_index = self.ui.recipe_list.currentIndex().row()
        if selected_index >= 0:
            self.update_fields()

    def select_ingredient(self):
        recipe_index = self.ui.recipe_list.currentIndex().row()
        ingredient_index = self.ui.ingredients_list.currentIndex().row()
        if recipe_index >= 0 and ingredient_index >= 0:
            ingredient = self.recipes[recipe_index].ingredients[ingredient_index]
            self.ui.ingredient_name_field.setText(ingredient.name)
            self.ui.amount_field.setText(ingredient.amount)

    def update_recipe_list(self):
        self.ui.recipe_list.clear()
        self.ui.recipe_list.addItems([recipe.name for recipe in self.recipes])

    def update_ingredients_list(self):
        recipe_index = self.ui.recipe_list.currentIndex().row()
        if recipe_index >= 0:
            self.ui.ingredients_list.clear()
            self.ui.ingredients_list.addItems([ingredient.name for ingredient in self.recipes[recipe_index].ingredients])

    def update_fields(self):
        selected_index = self.ui.recipe_list.currentIndex().row()
        if selected_index >= 0:
            recipe = self.recipes[selected_index]
            self.ui.ingredients_list.clear()
            self.ui.ingredients_list.addItems([ingredient.name for ingredient in recipe.ingredients])
            self.ui.ui.ingredient_name_field.clear()
            self.ui.ui.amount_field.clear()
            self.ui.directions_area.setText(recipe.directions)

    def update_selected_ingredient(self):
        recipe_index = self.ui.recipe_list.currentIndex().row()
        ingredient_index = self.ui.ingredients_list.currentIndex().row()
        if recipe_index >= 0 and ingredient_index >= 0:
            new_name = self.ui.
