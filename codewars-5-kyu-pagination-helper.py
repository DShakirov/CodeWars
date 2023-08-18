class PaginationHelper:
    
    def __init__(self, arr, items_per_page):
        self.arr = arr
        self.items_per_page = items_per_page

    def page_count(self):
        if len(self.arr)%self.items_per_page == 0:
            return len(self.arr)/self.items_per_page
        else:
            return int(len(self.arr)/self.items_per_page) + 1
        
    def item_count(self):
        return len(self.arr)

    def page_item_count(self, page_index):
        if page_index < 0:
            return -1
        elif page_index < self.page_count() - 1 :
            return self.items_per_page
        elif page_index == self.page_count() -1:
            return len(self.arr) - ( page_index)*self.items_per_page
        else:
            return -1
    
    def page_index(self, item_index):
        print(item_index, len(self.arr))
        if item_index > len(self.arr) -1   or item_index < 0 or not self.arr:
            return -1
        return int(item_index/self.items_per_page)


#helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper = PaginationHelper([1,2,3,4], 4)
#print(helper.page_count())
#print(helper.item_count())
#print(helper.page_item_count(-1))
print(helper.page_index(4))
