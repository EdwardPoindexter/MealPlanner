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
   mealPicks = []
   for meals in mealsListDict:
     if meals["type"] == "dinner":
         if meals["vegetarian"] == "yes":
           mealListVeg.append(meals["name"])
         else:
           mealListMeat.append(meals["name"])
   mealPicksVeg = mpf.genmealplan(mealListVeg, (4+1))
   tuesdaysPick = mealPicksVeg[0]
   mealPicksMeat = mpf.genmealplan(mealListMeat, (3+1))
   mealPicks = mealPicksVeg[1:4] + mealPicksMeat[0:3]
   #mealPicks = mealPicksVeg[1:3]
   #[mealPicks.append(item) for item in mealPicksMeat[0:2]]
   random.shuffle(mealPicks)
   mealPlan.append(mealPicks[0])
   mealPlan.append(tuesdaysPick)
   mealPlan = mealPlan + mealPicks[1:6]
   #[mealPlan.append(item) for item in mealPicks[1:5]]
   print(mealPlan) #for test
   
   #request substitute meals 
   finalMealPlan = mpf.requestforsubstitute(mealsListDict, mealPlan, mealPicksVeg[-1], mealPicksMeat[-1])
   # grab ingredient list from weekly meal list
   shoppingList = mpf.geningredientslist(mealsListDict, finalMealPlan)
   #print(shoppingList) #for test

   #write list to file
   ll = open('foodlist.txt',"w")
   ll.write("**************Meals of the week****************\n")
   day = 0 
   for items in finalMealPlan:
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
