# JavaScript Web jQuery Project

Welcome to the JavaScript Web jQuery project! In this project, you'll be working with DOM manipulation using JavaScript and jQuery. Below are the tasks and requirements to guide you through the project.

## Requirements

- **Editors**: You are allowed to use vi, vim, or emacs.
- **Compatibility**: Your code will be interpreted on Chrome (version 57.0).
- **New Line**: All your files should end with a new line.
- **README.md**: A README.md file at the root of the project folder is mandatory.
- **Code Style**: Your code should be semistandard compliant with the flag --global $: `semistandard *.js --global $`.
- **JQuery Version**: You must use JQuery version 3.x.
- **Variable Usage**: You are not allowed to use `var`.
- **HTML Reload**: HTML should not reload for each action, including DOM manipulation, updating values, and fetching data.

## More Info

### Import JQuery

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## Tasks

| Task | Description |
| ---- | ----------- |
| **0. No JQuery** | Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):<br>- Use `document.querySelector` to select the HTML tag.<br>- Don't use the JQuery API. |
| **1. With JQuery** | Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **2. Click and turn red** | Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header:<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **3. Add .red class** | Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag DIV#red_header:<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **4. Toggle classes** | Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:<br>- The `<header>` element must always have one class: red or green, never both, and never empty.<br>- If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green, and vice versa.<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **5. List of elements** | Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item:<br>- The new element must be: `<li>Item</li>`.<br>- The new element must be added to `UL.my_list`.<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **6. Change the text** | Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on DIV#update_header:<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **7. Star wars character** | Write a JavaScript script that fetches the character name from the URL: [https://swapi-api.alx-tools.com/api/people/5/?format=json](https://swapi-api.alx-tools.com/api/people/5/?format=json):<br>- The name must be displayed in the HTML tag DIV#character.<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **8. Star Wars movies** | Write a JavaScript script that fetches and lists the title for all movies from the URL: [https://swapi-api.alx-tools.com/api/films/?format=json](https://swapi-api.alx-tools.com/api/films/?format=json):<br>- All movie titles must be listed in the HTML tag UL#list_movies.<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API. |
| **9. Say Hello!** | Write a JavaScript script that fetches from [https://hellosalut.stefanbohacek.dev/?lang=fr](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays the value of hello from that fetch in the HTML tag DIV#hello:<br>- The translation of “hello” must be displayed in the HTML tag DIV#hello.<br>- Don't use `document.querySelector` to select the HTML tag.<br>- Use the JQuery API.<br>- Your script must work when imported from the `<head>` tag. |

### 0. No JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):

- Use `document.querySelector` to select the HTML tag.
- Don't use the JQuery API.

### 1. With JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):

- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 2. Click and turn red

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header:

- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 3. Add .red class

Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag DIV#red_header:

- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 4. Toggle classes

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:

- The `<header>` element must always have one class: red or green, never both, and never empty.
- If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green, and vice versa.
- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 5. List of elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item:

- The new element must be: `<li>Item</li>`.
- The new element must be added to `UL.my_list`.
- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 6. Change the text

Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on DIV#update_header:

- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 7. Star wars character

Write a JavaScript script that fetches the character name from the URL: [https://swapi-api.alx-tools.com/api/people/5/?format=json](https://swapi-api.alx-tools.com/api/people/5/?format=json):

- The name must be displayed in the HTML tag DIV#character.
- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 8. Star Wars movies

Write a JavaScript script that fetches and lists the title for all movies from the URL: [https://swapi-api.alx-tools.com/api/films/?format=json](https://swapi-api.alx-tools.com/api/films/?format=json):

- All movie titles must be listed in the HTML tag UL#list_movies.
- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.

### 9. Say Hello!

Write a JavaScript script that fetches from [https://hellosalut.stefanbohacek.dev/?lang=fr](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays the value of hello from that fetch in the HTML tag DIV#hello:

- The translation of “hello” must be displayed in the HTML tag DIV#hello.
- Don't use `document.querySelector` to select the HTML tag.
- Use the JQuery API.
- Your script must work when imported from the `<head>` tag.

## Author

[NEAZYIT](https://github.com/NEAZYIT)
