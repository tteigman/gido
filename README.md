### GIDO toolkit

#### Welcome to the Garbage in Data Out Toolkit

## FAQ

### What is this?
Read any type of "structured" data and output in a tabular format. 

### Who is this for?
- Transforming client reports to input into a standardized system
- Migrate lots of messy data into a clean system.

### How does that even work?
When this is done manually someone will look over the data (commonly in Excel) and start performing manipulations to create a standard tabular layout. Depending on the input data this can be quite laborious. I'm proposing using statistical techniques to determine header information and pattern recognition to classify the data.

### How can this be accomplished if this problem requires very high if not exact accuracy?
Consider a jigsaw puzzle, it's possible you won't get it right but it will be obvious that you're wrong. Also, as more pieces are put into place the puzzle will become easier. The assumption is while the input data is not structured for inputting into database, there is structure to it and rows or sections of cells will fit together analogous to a puzzle. 

## Techniques
#### Header guessing
Have you ever accidently sorted your headers into your data in Excel? Besides not having headers, it's pretty obvious that the headers don't fit with the rest of the data. Even in a dataset that has duplicated headers we can determine which data doesn't fit by extracting features that differentiate the header/s from the rest of the data.
