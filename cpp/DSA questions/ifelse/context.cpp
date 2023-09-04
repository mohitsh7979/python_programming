#include <bits/stdc++.h>
using namespace std;

int main()
{
	// your code goes here

	int t;
	cin >> t;

	for (int i = 0 ; i < t ; i++)
	{

		int n;
		cin >> n;
		int counter = 0;

		while (n > 0)
		{

			int a = n % 10;
			n = n / 10;

			if (a == 4)
			{

				counter++;
			}
		}
		cout << counter << endl;
	}

	return 0;
}
