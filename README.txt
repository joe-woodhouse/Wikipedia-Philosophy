Tests the theory that most Wikipedia pages will end up on the "Philosophy" page if you repeatedly follow the first "legit" link on each page.

Legit links are defined as not parenthetical, not Wiki comments, not sidebar text, and not internal Wikipedia links like "Help:*" or "(disambiguation)".

You can supply the URL yourself to any given start page; it will pick one at random otherwise.

Requires "requests" and "BeautifulSoup" modules.

I've written for clarity of code, not performance. There are a number of areas that could obviously benefit from refactoring. The main one is that this doesn't use Wiki APIs and is simply going in via regular URL requests.


Still to do:

- Detect infinite loops. Minor work.
- Use Wiki API calls. Major work.
- Monte Carlo simulation: run for arbitary # of random starts and collect stats. Major work.