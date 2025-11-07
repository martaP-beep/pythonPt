

class Stack:
    def __init__(self):
        self.stack = []
        pass
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty() :
            return self.stack.pop()
    def peek(self):
        if not self.is_empty() :
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

class BrowserHistory:
    def __init__(self):
        self.history = Stack()
        self.current_page = None
        pass

    def print_history(self):
        print(self.history.stack)
    
    def go_page(self, url):
        
        self.history.push(self.current_page)
        self.current_page = url
    
    def go_back(self):
        previous_page = self.history.pop()
        if previous_page is not None:
            self.current_page = previous_page

browser = BrowserHistory()
browser.go_page("strona 1")


browser.go_page("strona 2")
browser.go_page("strona 3")
browser.go_page("strona 4")
browser.print_history()
browser.go_back()
browser.print_history()

browser.go_back()
browser.print_history()

browser.go_back()
browser.print_history()