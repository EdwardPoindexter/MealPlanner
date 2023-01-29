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




