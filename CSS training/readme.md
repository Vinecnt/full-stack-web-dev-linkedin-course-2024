# CSS Training Notes

- [CSS Training Notes](#css-training-notes)
  - [Getting Started](#getting-started)
  - [Core Concepts](#core-concepts)

## Getting Started
- Relative and absolute paths
  - similar to file directories
  - Don't embedded other third party website resources
    - aka hot linking
- By default images are displayed as the same size as source images size
- retina images; apple trade marked high density pixel screensg
- 
- Inline Css
  - should be used sparingly and difficult to maintain
- Internal Css
  - can use style element tag, but still bad for same reason as inline css
- external css
  - link tag, rel to style sheet, href path to css file
  - easy to manage
  - seperates from html
- Naming conventions
  - styles.css
  - name after project then append .css
## Core Concepts
- W3C spec
  - W3C
    - Responsible for CSS specification
    - Multiple levels and modules
    - levels no longer refer to versions
    - Status codes are colorized
- CSS syntax
  - Declaration block
    - contains one or more style rules enclosed in curly brackets
    - Selector
      - specifies which html element to apply style to 
  - Declarations
    - CSS Style rule
    - use property value pairs to tell
    - seperated by colon and line ends with semi colon
  - Some property have shorthand and longhand
    - ex: padding
    - long hand can be used for specifying just one of the sub properties
    - /* */ for commenting
  - White Space
    - add space between selector names
    - white space matters in shorthand
    - can also use a linter
  - CSS Property, Values, Units
    - color
      - color, hex, rgb
  - Numeric data types
    - used with or without units
  - Length
    - distance value 
    - absolute length
      - fixed based units
    - Relative Units
      - length based on a anohter element
        - em
        - vw
        - vh
  - Keywords
    - textual data types
    - predefined values
    - In the css spec
      - ex: blue, dashed
  - Functions
    - can be complex
    - start with name of function
      - ex: calc, rotate, rgb
  - Pseudo-classes
    -  keyword added to a selector that specifies a special state of the selected element
    -  ex: :hover can be used to select a button when user's pointer hovers over the button
  - Pseudo-element is a keyword added to selector to style a specific part of the selected element
    -  ex: ::first-line can be used to change the font of the first paragraph line
    -  can only have one pseudo-element in a selector
    -  ex: p:hover::first-line
    -  selects the first line of a paragraph when the paragraph itself is being hovered
- Color property
  - different color values
  - keywords
    - ex: red, blue, green
    - ex: oldlace, darkslategray
      - check docs for full list
  - colours.neilorangepeel
  - rgb value functions
    - old syntax uses comma
    - new syntax comma less
  - hex values for colors
    - can even add a transparency value with additional 0 to FF
  - How to pick colors
    - canva dot com
  - Type Selectors
    - ex: body
  - Universal selectors
    - asterisk
    - becareful
- ID Selector
  - Match to single unique element
  - technically can put same id value in multiple elements, but not technically valid code
- Multiple classes
  - can have multiple class on one element
  - must be seperated by space and contained within the quotes
  - order of class names doesn't matter
- Combining Selectors
  - join the selectors with no spaces
    - styles are only applied when all classes are added to element
  ```css
  <!-- only applies if both classes pressent-->
  .big.tall {
    width: 100px
    height: 200px
  }

  <\p class="big tall">will be wide and tall</p>
  ```
- Descendant combinators and selector list
  - The DOM
    - Document object model
    - relationship between elements in html page
    - parent, child, descendant, sibling
      - like in a graph
  - selectors 
     ```
     <!-- applies in this specific order -->
     ancestor descedant {
     }
     ```
- Background property
  - background is actually shorthand for many property
  - long hand properties
    - background-color
    - background-image
    - background-no-repeat
    - background-position
      - can use box coordinates
      - also bottom center
    - background-size
      - cover stretches
- Shorthand sytnax
  - order doesn't matter
  - except when using background size
  - background size must be declared with a background-position value seperated with a slash
    - bad ex: center cover
    - good ex: center/cover
  - if no background position
    - just add background-size: cover afterwards 
  - it's a pain just use longhand
- Inheritance and cascade
  - browser read styles top to bottom
  - conflicting rules are resolved by declarations loaded last
- Specificity over rides Css rules
  - determines which CSS rule takes precedence when style conflict based on the type and number of selectors used
    - some selectors have more weight than other
    - higher specificity have more weight
  - tiers high to low
    - id
    - class
    - type
    - universal
  - Calculations
    - number of id selectors
    - number of class selectors
    - number of type selectors
    - number for each count are concatenated for a final specificity values
    - Ex: .classname p a
      - specificit = 012
      - 0 ids
      - 1 class
      - 2 type selectors
  - Inheritance
    - descendant elements will inherit styles from ancestor
    - cascade rule means last declaration will be displayed if there's a conflict
    - more specific selector will override both inheritance and the cascade
  - The over of all three
    - !important
  - overriding important requires !important with more specficity
    - bad practice 
    - avoid if can