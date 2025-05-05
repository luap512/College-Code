#include "ArrayBag.h"
#include <iostream>
#include <cstddef>
#include <vector>

//----------------------------------------------------------------------------------------------------------------         ----------------

// search ITERATIVE@@@
template <class ItemType>
int ArrayBag<ItemType>::binarySearch(const ItemType &anEntry)
{

   std::cout << "SEARCHING BAG.....\n";
   // initialize bottom of list
   int low = 0;
   // initialize top of list
   int high = itemCount - 1;
   // while the list hasent been traversed
   while (low <= high)
   {
      // initialize middle of list
      int mid = (low + high) / 2;
      // compare entry to middle of list
      if (anEntry == items[mid])
      {
         // found
         std::cout << "Item found!! \n";
         return mid;
      }
      else if (anEntry < items[mid])
      {
         // entry is in top of list, move bottom and start incrimenting
         low = mid + 1;
      }
      else
      {
         // entry is in top of list, move top and start incrimenting
         high = mid - 1;
      }
   }
   return -1;

} // end isEmpty

//-----------------------------------------------------------------------------------------  ---------------------------------------

// search recursive@@@
template <class ItemType>
int ArrayBag<ItemType>::searchRecursive(const ItemType &anEntry)
{
   std::cout << "SEARCHING BAG.....\n";
   int low = (itemCount - itemCount);
   int high = (itemCount);
   // This is the part where i'm confused.
   // obviously with a recursive fucntion we cant reset the high and low
   // values every time we call this function because then we arent
   // iterating therough the bag and an infinite loop occur

   // initialize middle of list
   int mid = low + (high - low) / 2;
   // compare entry to middle of list
   if (anEntry == items[mid])
   {
      // found
      return mid;
   }
   else if (anEntry < items[mid])
   {
      std::cout << "item is in bottom half \n";
      return searchRecursive(high = mid - 1); // These arguments must be incorrect?
   }
   else
   {
      std::cout << "item is in top half \n";
      return searchRecursive(low = mid + 1); // These arguments must be incorrect?
   }

} // end isEmpty
// :-((((( I dont understand how to properly manipulate the high and low variables
// when I can only pass 'anEntry' to searchRecursive. Also its sunday and I've got work this afternoon so
// i'm basically out of time :((

//---------------------------------------------------------------------------------------------------------------------------------------------------

// Displays current contents of bag@@@
template <class ItemType>
void ArrayBag<ItemType>::displayContents()
{
   std::cout << "\n--DISPLAYING BAG CONTENTS--\n";

} // end isEmpty

// Gets data from user and validates it, returns user input (integer 1-6)@@@
template <class ItemType>
int ArrayBag<ItemType>::getUserData()
{
   // initialize choice variable
   int choice;
   // while loop to ask user for data until input
   // is valid
   while (true)
   {
      // get data from user
      std::cout << "-------------------------\n";
      std::cout << "ENTER YOUR OPTION:\n";
      std::cin >> choice;
      std::cout << "-------------------------\n";

      // check if user input is valid
      if (!std::cin.fail())
      {
         // check is usr input is between 1 and 6
         if (choice > 0 && choice < 7)
         {

            // print valid input message exit loop and return user choice
            std::cout << "USER SELECTS OPTION: " << choice << "\n";
            return choice;
            break;
         }
         else
         {
            // print error message continue loop
            std::cout << "Invalid Choice: " << choice << "\n(Try integers 1-6)\n";
         }
      }
      else
      {
         // print error message continue loop
         std::cout << "not an integer!\n(Try integers 1-6)\n";
      }
   }
}
// end isEmpty
//------------------------------------------------------------------------------------------------------------------------------------

// Displays the menu@@@
template <class ItemType>
void ArrayBag<ItemType>::displayMenu()
{
   // consecutive print statements to show
   // the menu to user
   std::cout << "\n------->MENU<--------------\n";
   std::cout << "1: DISPLAY CONTENTS OF BAG \n";
   std::cout << "2: ADD VALUES TO BAG\n";
   std::cout << "3: REMOVE VALUES FROM BAG\n";
   std::cout << "4: SORT BAG \n";
   std::cout << "5: SEARCH BAG (ITERATIVE)\n";
   std::cout << "6: SEARCH BAG (RECURSIVE)\n";
   std::cout << "-------------------------\n";
} // end isEmpty
// --------------------------------------------------------------------------------------------------------------------------------

template <class ItemType>
ArrayBag<ItemType>::ArrayBag() : itemCount(0), maxItems(DEFAULT_CAPACITY)
{
} // end default constructor

template <class ItemType>
int ArrayBag<ItemType>::getCurrentSize() const
{
   return itemCount;
} // end getCurrentSize

template <class ItemType>
bool ArrayBag<ItemType>::isEmpty() const
{
   return itemCount == 0;
} // end isEmpty

// --------------------------------------------------------------------------------------------------------------------------------
// add items to the bag@@@
template <class ItemType>
bool ArrayBag<ItemType>::add(const ItemType &newEntry)
{
   bool hasRoomToAdd = (itemCount < maxItems);
   if (hasRoomToAdd)
   {
      items[itemCount] = newEntry;
      itemCount++;
   } // end if

   return hasRoomToAdd;
} // end add

template <class ItemType>
bool ArrayBag<ItemType>::remove(const ItemType &anEntry)
{
   int locatedIndex = getIndexOf(anEntry);
   bool canRemoveItem = !isEmpty() && (locatedIndex > -1);
   if (canRemoveItem)
   {
      itemCount--;
      items[locatedIndex] = items[itemCount];
   } // end if

   return canRemoveItem;
} // end remove

template <class ItemType>
void ArrayBag<ItemType>::clear()
{
   itemCount = 0;
} // end clear

template <class ItemType>
int ArrayBag<ItemType>::getFrequencyOf(const ItemType &anEntry) const
{
   int frequency = 0;
   int curIndex = 0; // Current array index
   while (curIndex < itemCount)
   {
      if (items[curIndex] == anEntry)
      {
         frequency++;
      } // end if

      curIndex++; // Increment to next entry
   }              // end while

   return frequency;
} // end getFrequencyOf

template <class ItemType>
bool ArrayBag<ItemType>::contains(const ItemType &anEntry) const
{
   return getIndexOf(anEntry) > -1;
} // end contains

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Returns a vector containing all items in the bag@@@
template <class ItemType>
std::vector<ItemType> ArrayBag<ItemType>::toVector() const
{
   std::vector<ItemType> bagContents;
   for (int i = 0; i < itemCount; i++)
      bagContents.push_back(items[i]);

   return bagContents;
} // end toVector

// private
template <class ItemType>
int ArrayBag<ItemType>::getIndexOf(const ItemType &target) const
{
   bool found = false;
   int result = -1;
   int searchIndex = 0;

   // If the bag is empty, itemCount is zero, so loop is skipped
   while (!found && (searchIndex < itemCount))
   {
      if (items[searchIndex] == target)
      {
         found = true;
         result = searchIndex;
      }
      else
      {
         searchIndex++;
      } // end if
   }    // end while

   return result;
} // end getIndexOf
