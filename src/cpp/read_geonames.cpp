#include <fstream>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

const float eps = 0.000001;

bool isValidLatitude(float lat)
{
    if (-90 - eps < lat && lat < 90 + eps)
    {
        return true;
    }

    return false;
}

bool isValidLongitude(float lon)
{
    if (-180 - eps < lon && lon < 180 + eps)
    {
        return true;
    }

    return false;
}

void readLines(char *inputFile, bool inMemory)
{
    ifstream fileStream(inputFile);
    string line;
    int lineCount = 0;
    vector<float> x;
    vector<float> y;
    for (; getline(fileStream, line); lineCount++)
    {
        stringstream lineStream(line);
        string token;
        float lat;
        float lon;
        for (int tokenIndex = 0; getline(lineStream, token, '\t') && tokenIndex < 6; tokenIndex++)
        {
            switch (tokenIndex)
            {
                case 4:
                    lat = atof(token.c_str());
                    if (inMemory && isValidLatitude(lat))
                    {
                        y.push_back(lat);
                    }                    
                    break;
                case 5:
                    lon = atof(token.c_str());
                    if (inMemory && isValidLongitude(lon))
                    {
                        x.push_back(lon);
                    }
                    break;
            }
        }
    }
    cout << lineCount << " lines read." << endl;
    if (inMemory)
    {
        cout << x.size() << " coordinates read." << endl;
    }
}


int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cout << "Usage: " << argv[0] << " <file>" << endl;
        return -1;
    }

    bool inMemory = false;
    if (2 < argc)
    {
        if ("in-memory" == string(argv[2]))
        {
            inMemory = true;
        }
    }

    readLines(argv[1], inMemory);

    return 0;
}
