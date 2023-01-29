#!/usr/bin/python

import json
import random
import mealPlanFunctions as mpf

def main():
   #list
   dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   # load json file /
   f = open('meals.json', "r")
   #print(f)
   mealsDict = json.load(f)
   f.close
   mealsListDict = mealsDict["meals"]

   # grab dinner list from json file randomly pick from veg and meat meals
   # create a list for 7 days with tuesday meal being veg
   mealListVeg = []
   mealListMeat = []
   mealPlan = []
   for meals in mealsListDict:
     if meals["type"] == "dinner":
         if meals["vegetarian"] == "yes":
           mealListVeg.append(meals["name"])
         else:
           mealListMeat.append(meals["name"])
   mealPicksVeg = mpf.genmealplan(mealListVeg, 4)
   tuesdaysPick = mealPicksVeg[0]
   mealPicksMeat = mpf.genmealplan(mealListMeat, 3)
   mealPicks = mealPicksVeg[1:] + mealPicksMeat
   random.shuffle(mealPicks)
   mealPlan.append(mealPicks[0])
   mealPlan.append(tuesdaysPick)
   mealPlan = mealPlan + mealPicks[1:]
   print(mealPlan)

   # grab ingredient list from weekly meal list
   shoppingList = mpf.geningredientslist(mealsListDict, mealPlan)
   print(shoppingList)

   #write list to file
   ll = open('foodlist.txt',"w")
   ll.write("**************Meals of the week****************\n")
   day = 0 
   for items in mealPlan:
      ll.write("******"+dayOfTheWeek[day]+"*********\n")
      ll.write(items + "\n")
      day += 1
   ll.close
   lt = open('shoppinglist.txt',"w")
   lt.write("\n**********Shopping list of the week**********\n")
   for items in shoppingList:
      lt.write(items + "\n")
   lt.close


if __name__ == "__main__":
    main()
