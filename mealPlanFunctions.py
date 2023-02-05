#!/usr/bin/python

import random

def genmeallist(mealsListDict, mealType):
   """
   find all of the names in the meal plan file given a meal type
   """
   mealList = []
   for meals in mealsListDict:
       if meals["type"] == mealType:
           mealList.append(meals["name"])
   return mealList

def genmealplan(mealList,numDays):
   """
   create a list of dinners for a week
   """
   mealPlanList = random.sample(mealList, numDays)

   return mealPlanList

def geningredientslist(mealsListDict, mealList):
   """
   list all of the ingredients for in a given list
   """
   allIngredientsList = []
   for meals in mealsListDict:
       if meals["name"] in mealList:
           for items in meals["ingredients"]:
              allIngredientsList.append(items)
   #remove repeated ingredients
   ingredientsList = list(dict.fromkeys(allIngredientsList))
   #print(allIngredientsList)

   return ingredientsList

def requestforsubstitute(mealsListDict, mealPlan, subMealVeg, subMealMeat):
   """
   provide option to substitute a meal from the random generated
   mealPlan
   """
   #print meal plan with number options
   finalMealPlan = mealPlan
   i = 1
   dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

   print('******* Preliminary MealPlan **********\n')
   for meal in mealPlan:
        print(str(i) + '. ' + dayOfTheWeek[i-1] + ' : ' + meal +'\n')
        i += 1
   print('\n')
   #ask if a substitution is desired 
   subChoice = input('Enter meal number to substitute or 99 to accept meal plan:')
   subChoice = int(subChoice)
   #check range of input
   if subChoice == 99:
      print('Meal Plan accepted, NO CHANGE made \n')
      print('\n')
   else:            
      if subChoice <= 7:
            for meal in mealsListDict:
                if meal["name"] == mealPlan[subChoice-1]:
                    #determine if meal is veg or non veg
                    if meal["vegetarian"] == "yes":
                        finalMealPlan[subChoice-1] = subMealVeg
                    else:
                        finalMealPlan[subChoice-1] = subMealMeat
            print('Substituting ' + dayOfTheWeek[subChoice-1] + 'meal \n')
            print('\n')
      else:                  
         print('Selection Not Valid, NO CHANGE to mealPlan made \n')
         print('\n')
        
      #print out new list
      print('******* Final MealPLan **********\n')
      i = 0 
      for meal in finalMealPlan:
         print(dayOfTheWeek[i] + ' : ' + meal +'\n')
         i += 1
      print('\n')    
   return finalMealPlan