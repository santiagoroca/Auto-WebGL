# AutoWebGL

AutoWebGL is a Automation tool written on top of Selenium, covering WebGL based projects, allowing the developer to run multiple test based on image comparison at low level code, while easing the process of writing and injecting scripts.

### Installation
```sh
$ pip install autowebgl
```

### Example of use

```python
from autogl import test
from autogl import autoglconfig

autoglconfig.configurate({
        "url": "https://local.server.com"
})

@test({"waitBeforeExecute": 10000, "waitAfterExecute": 1000})
def should_walk_aroun_the_scene(browser):
        browser.mouseDownAt(100, 100, "viewer")
        browser.mouseMoveFromTo(500, 0, 500, 800, "viewer")
        browser.mouseUpAt(200, 200, "document")
```

### Creating the test data

After succesfuly writing your first test, you need to create the test data, a point in time when you are sure the browser will answer your described behaviour correctly.

```sh
$ python testcases.py --capture
```

This command will run every test, capturing the final result of each and storing it under 'cases' folder.

### Running the tests

After you have created and captured all your test data, you can run all your cases with the next command.
```sh
$ npython testcases.py
```

### Browser Object
* mouseDownAt(x_position, y_position, target_element)
* mouseMoveFromTo(x_origin_position, y_origin_position, x_destiny_position, y_destiny_position, target_element)
* mouseUpAt(x_position, y_position, target_element)
* dragAndDropFromTo(x_origin_position, y_origin_position, x_destiny_position, y_destiny_position, target_element)
* exectue(text_script) 

### Test parameters
* waitBeforeExecute [not required][int] milliseconds number representing the sleep time before running the test case
* waitAfterExecute [not required][int] milliseconds number representing the sleep time after running the test case and before running the comparison

### AutoWebGL Config Parameters
* url [required][str] String describing the url used for each case



