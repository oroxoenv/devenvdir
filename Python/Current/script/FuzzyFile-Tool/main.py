import os

from icecream import ic
from fuzzywuzzy import fuzz


root_dir = input( 'Enter the root  directory for your search: ' )

file_types = input( 'Enter the file endings to look for ( Separate by spaces ) ( Empty = All ) : ' )

fuzzy_search = input( 'Enter a fuzzy search query ( Empty = None ) : ' )


file_types = file_types.split( sep = ' ' )


for root, dirs, files in os.walk( top = root_dir ) :
    for name in files :
        if (
                name.endswith( tuple( ft for ft in file_types ) )
                or
                file_types[ 0 ] == ''
        ) :
            if (
                    fuzz.token_sort_ratio(
                        s1    = fuzzy_search.lower(),
                        s2    = name.lower()
                    ) > 50
                    or
                    fuzzy_search == ''
            ) :
                ic( root + os.sep + name )
