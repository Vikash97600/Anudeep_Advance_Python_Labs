#  Q.1 --> Create a class Employee that manages employee details:
#   1. Instance Attributes: name: The employee's name. salary: The employee's salary. position: The employee's position. 
#   2. Methods: promote(self, new_position): Updates the employee's position.  update_salary(self, new_salary): Updates the employee's salary.  display_info(self): Displays the employee's name, position, and salary'

class Employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
    def promote(self, new_position):
        self.position=new_position
        return new_position
    def update_salary(self, new_salary):
        self.salary=new_salary
        return new_salary
    def display_info(self):
        return f"Name:{self.name}, Salary:{self.salary}, Promote:{self.position}"

emp=Employee("Vikash",80000,"Developer")
print(f"Employee Details are : {emp.display_info()}")
print(f"Updating the position  and salary of {emp.name} as :{emp.promote("HR")} and {emp.update_salary(100000)}")
print(f"After updating the details of employee {emp.name} is : {emp.display_info()}")


# Q.2-->  Create a class MovieLibrary that manages a collection of movies:
# 1. Class Attribute: available_movies: A list of all movies available in the library. 
# 2. Instance Attributes: member_name: The name of the library member. borrowed_movies: A list of movies borrowed by the member. 
# 3. Methods: borrow_movie(self, movie): Borrows a movie from the library if available. return_movie(self, movie): Returns a movie to the library.  view_borrowed_movies(self): Prints a list of movies borrowed by the member

class MovieLibrary:
    available_movies=['Chhava','Devera','Bahubali','Bahubali 2','Hanuman']
    totalMovie=5
    def __init__(self, member_name, borrowMovies):
        self.member_name = member_name
        self.borrowMovies = borrowMovies

    def borrow_movie(self, movie):
        if movie in MovieLibrary.available_movies:
           self.borrowMovies.append(movie)
           MovieLibrary.available_movies.remove(movie)
           MovieLibrary.totalMovie -= 1
           return f"{self.member_name} has borrowed '{movie}'"
        else:
          return "Movie that you want is not available"

    def return_movie(self, movie):
        if movie in self.borrowMovies:
          self.borrowMovies.remove(movie)
          MovieLibrary.available_movies.append(movie)
          MovieLibrary.totalMovie += 1
          return f"{self.member_name} has returned a movie '{movie}'"
        else:
          return f"{self.member_name} has not borrowed a movie '{movie}'"

    def view_borrowed_movies(self):
      return f"{self.member_name} has borrowed {self.borrowMovies}"


member1 = MovieLibrary("Vikash", ["Chhava", "Devera"])

print(member1.view_borrowed_movies())
print(member1.borrow_movie("Bahubali"))
print(member1.borrow_movie("Hanuman"))
print(member1.return_movie("Devera"))
print(member1.return_movie("Bahubali 2"))
print(member1.view_borrowed_movies())