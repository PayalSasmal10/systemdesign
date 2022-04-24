from django.shortcuts import render
from abc import abstractmethod

# Create your views here.
class RestaurantService:
    @abstractmethod
    def SignUp(self,email, name, password, contactno):
        pass
    
    @abstractmethod
    def restaurantSignIn(self, email, password):
        pass

    @abstractmethod
    def restaurantAdd(self, restaurantname, foodmenu):
        
        @abstractmethod
        def foodmenu(self, foodname, description, picture):
            pass


class CustomerService:

    @abstractmethod
    def SignUp(self, first_name, second_name, email, password):
        pass
    
    @abstractmethod
    def SignIn(self, email, password):
        pass
    







