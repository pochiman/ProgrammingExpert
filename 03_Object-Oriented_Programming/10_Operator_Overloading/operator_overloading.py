# class Page:
#   def __init__(self, words, page_number):
#     self.words = words
#     self.page_number = page_number

#   def __add__(self, other):
#     new_words = self.words + " " + other.words
#     new_page_number = max(self.page_number, other.page_number) + 1
#     return Page(new_words, new_page_number)

# page1 = Page("Tim is a great instructor!", 1)
# page2 = Page("This is another page.", 2)
# page3 = page1 + page2
# print(page3.words, page3.page_number)

########## ########## ########## ########## ##########

# class StoreItem:
#   TAX = 0.13

#   def __init__(self, name, price):
#     self.name = name
#     self.price = price
#     self.after_tax_price = 0
#     self.set_after_tax_price()

#   def set_after_tax_price(self):
#     self.after_tax_price = round(self.price * (1 + self.TAX), 2)

#   def __sub__(self, discount):
#     return StoreItem(self.name, self.price - discount)

#   def __mul__(self, value):
#     return StoreItem(self.name, self.price * value)

# bread = StoreItem("Bread", 7)
# discounted_bread = bread * 0.5
# print(discounted_bread.after_tax_price)

########## ########## ########## ########## ##########

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)

# line1 = Line((10, 5), (20, 10))
# line2 = line1 / 2
# print(line2.point1, line2.point2)

########## ########## ########## ########## ##########

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)
  
#   def __floordiv__(self, factor):
#     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
#     new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
#     return Line(new_point1, new_point2)

# line1 = Line((10, 5), (20, 9))
# line2 = line1 // 2
# print(line2.point1, line2.point2)

########## ########## ########## ########## ##########

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)
  
#   def __floordiv__(self, factor):
#     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
#     new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
#     return Line(new_point1, new_point2)

#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)

# line1 = Line((10, 5), (20, 9))
# print(len(line1))

########## ########## ########## ########## ##########

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)



# line1 = Line((10, 5), (20, 9))
# line2 = Line((10, 5), (20, 9))
# line2 = line1
# print(line1 == line2)
# print(id(line1) == id(line2))
# print(line1 is line2)
# print(line1 != line2)

########## ########## ########## ########## ##########

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)

#   def __eq__(self, other):
#     if not isinstance(other, Line):
#       return False

#     return self.point1 == other.point1 and self.point2 == other.point2

#   def __ne__(self, other):
#     pass

# line1 = Line((10, 5), (20, 9))
# line2 = Line((10, 5), (20, 9))
# line2 = Line((9, 5), (20, 9))
# print(line1 == 3)
# print(line1 == line1)
# print(line1 == line2)

########## ########## ########## ########## ##########

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)

#   def __eq__(self, other):
#     if not isinstance(other, Line):
#       return False

#     return self.point1 == other.point1 and self.point2 == other.point2

#   def __ne__(self, other):
#     return not self.__eq__(other)

# line1 = Line((10, 5), (20, 9))
# line2 = Line((9, 5), (20, 9))
# print(line1 == line2)
# print(line1 != line2)

########## ########## ########## ########## ##########

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2

#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)

#   def __eq__(self, other):
#     if not isinstance(other, Line):
#       return False

#     return self.point1 == other.point1 and self.point2 == other.point2

#   def __ne__(self, other):
#     return not self.__eq__(other)

#   def __gt__(self, other):
#     return len(self) > len(other)

#   def __ge__(self, other):
#     return len(self) >= len(other)

#   def __lt__(self, other):
#     return len(self) < len(other)    

#   def __le__(self, other):
#     return len(self) <= len(other) 

# line1 = Line((10, 5), (20, 9))
# line2 = Line((9, 5), (20, 9))
# line2 = Line((20, 5), (20, 9))
# line2 = Line((10, 5), (20, 9))
# line2 = Line((0, 5), (20, 9))
# print(line1 > line2)
# print(line1 >= line2)

########## ########## ########## ########## ##########

class Page:
  def __init__(self, text, page_number):
    self.text = text
    self.page_number = page_number

  def __len__(self):
    return len(self.text)

  def __str__(self):
    # return self.text
    # return f"Page(text = {self.text}, page_number = {self.page_number})"
    return f"Page({self.text}, {self.page_number})"

  def __repr__(self):
    return self.__str__()


class Book:
  def __init__(self, title, author, pages, id_number):
    self.title = title
    self.author = author
    self.pages = pages
    self.id_number = id_number

  def __len__(self):
    return len(self.pages)

  def __str__(self):
    output = f"Book({self.title}, {self.author}, {self.id_number})"  
    
    for page in self.pages:
      output += "\n" + str(page)

    return output

  def __repr__(self):
    return f"Book(id_number={self.id_number})"


page1 = Page("Page 1!", 1)
page2 = Page("This is page 2.", 2)
book = Book("Tim is Great", "Tim", [page1, page2], 1)
# print(len(page1))
# print(len(page2))
# print(len(book))
# print(page1, page2)
# print(book)
# print(repr(book))
# print(repr([1, 2, 3, 4]))
# print(repr(1))
# print(repr(True))