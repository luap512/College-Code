#include <iostream>
#include <string>
#include "ArrayBag.h"

using namespace std;

void bagTester(ArrayBag<int> &bag);

int main()
{
	// variable for the option entered by the user
	int menuOption;
	// is the bag sorted
	bool sorted = false;

	// This is one way you can get values in the bag.
	// You could also read the values from a file.
	// You pick - but you should load up the bag with values.
	ArrayBag<int>
		bag;
	int items[] = {1, 33, 6, 9, 2, 65, 4, 29, 5, 8, 39, 88, 7, 25, 51, 3, 99, 14, 10, 11};

	cout << "\nAdding positive integers to the bag\n";
	for (int i = 0; i < 20; i++)
	{
		bag.add(items[i]);
	} // end for

	// This shows the client program invoking the new method "menu"
	// This function displays the menu
	bag.displayMenu();
	// let user select a menu option
	menuOption = bag.getUserData();
	// while menu is being displayed
	while (menuOption != 0)
	{
		// user selected option 1
		if (menuOption == 1)
		{
			// create a vector called currentContents to store the current contents of the bag
			vector<int> currentContents = bag.toVector();
			bag.displayContents();
			for (int number : currentContents)
			{
				cout << number << "\n";
			}
			// return to menu option
			bag.displayMenu();
			menuOption = bag.getUserData();
		} // end if

		// user selected option 2
		else if (menuOption == 2)
		{
			float addVal;
			cout << "\n--ADDING VALUES TO THE BAG--\n";
			cout << "Enter a new value to add to the bag: \n";
			// get value to add to the bag
			cin >> addVal;
			// check if bag is full before adding
			if (bag.add(addVal) == false)
			{
				cout << "Bag is full " << addVal << " not added to the bag\n";
			}
			else
			{
				bag.add(addVal);
				cout << "Filling the bag with " << addVal << " \n";
			}
			// return to menu option
			sorted = false;
			bag.displayMenu();
			menuOption = bag.getUserData();
		} // end if

		// user selected option 3
		else if (menuOption == 3)
		{
			float minusVal;
			cout << "\n--REMOVING VALUES FROM BAG--\n";
			cout << "Enter a value to remove from the bag: \n";
			// get value to add to the bag
			cin >> minusVal;

			// if value hasnt been removed let user know
			if (bag.remove(minusVal) == false)
			{
				cout << "Invalid entry - nothing removed from the bag\n";
			}
			else
			{
				// remove value and let user know
				bag.remove(minusVal);
				cout << "Removing " << minusVal << "s from the bag \n";
			}

			// bag has been modified and is no longer sorted
			sorted = false;
			// return to menu option
			bag.displayMenu();
			menuOption = bag.getUserData();

		} // end if

		// user selected option 4
		else if (menuOption == 4)
		{
			cout << "\n--SORTING BAG--\n";

			// create a vector with unsorted contents
			vector<int> unsortedContents = bag.toVector();
			// sort the vector
			sort(unsortedContents.begin(), unsortedContents.end(), greater<int>());
			// empty the bag
			bag.clear();
			// add the sorted vector to the bag
			for (int x = 0; x < unsortedContents.size(); x++)
			{

				bag.add(unsortedContents[x]);
			}

			// display the sorted vector
			cout << "(index 0 is at the top of the list)\n";
			cout << "The sorted contents of the bag: \n";

			for (int numbers : unsortedContents)
			{

				cout << numbers << "\n";
			}
			// return to menu option
			sorted = true;
			bag.displayMenu();
			menuOption = bag.getUserData();
		} // end if

		// user selected option 5
		else if (menuOption == 5)
		{
			// if sorted
			if (sorted == true)
			{
				int searchValue;
				cout << "SEARCHING FOR: \n";
				cin >> searchValue;
				cout << "\n--SEARCHING BAG (ITERATIVE)--\n";

				int entryIndex = bag.binarySearch(searchValue);
				cout << searchValue << " exists at index " << entryIndex << "\n";
			}
			else
			{
				cout << "Bag must be sorted first\n";
				sorted = false;
			}
			// return to menu option
			bag.displayMenu();
			menuOption = bag.getUserData();
		} // end if

		// user selected option 6
		else if (menuOption == 6)
		{
			// if sorted
			if (sorted == true)
			{
				int searchValueRecursive;
				cout << "SEARCHING FOR: \n";
				cin >> searchValueRecursive;
				cout << "\n--SEARCHING BAG (RECURSIVE)--\n";
				int entriesIndex = bag.searchRecursive(searchValueRecursive);
				cout << searchValueRecursive << " exists at: " << entriesIndex << "\n";
			}
			else
			{
				cout << "Bag must be sorted first\n";
				sorted = false;
			}

			// return to menu option
			bag.displayMenu();
			menuOption = bag.getUserData();
		} // end if
	}	  // end while

	return 0;

} // end main

void bagTester(ArrayBag<int> &bag)
{
	// This is just some sample code processing the bag.
	// You should remove this function from your program completely.
	cout << "The bag is not empty; isEmpty: returns " << bag.isEmpty() << endl;

	cout << "About to clear the bag, ";
	bag.clear();

	cout << "isEmpty: returns " << bag.isEmpty() << endl;
} // end bagTester
