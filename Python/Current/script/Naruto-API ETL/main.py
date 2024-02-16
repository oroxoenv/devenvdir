import os
import json
import time
import requests

import polars as pl

from icecream import ic
from abc import (
    abstractmethod,
    ABC,
)



class Utils:
    def __init__(
        self
    ) -> None:
        self.data_path: str = 'datas/'


    def get_dir( self ):
        ...


    def to_PolarsDataFrame( self, data: dict ) -> pl.DataFrame:
        df = pl.DataFrame( data = data )
        print( df )
        return df


    def to_JSONFile( self, json_struct: dict ):
        ...


    def convert_to_json(self, data: dict ) -> bool | None:
        current_dir: str = os.getcwd()
        debug: str = f'Current working directory: { current_dir }'
        ic( debug )

        listing_dir: list[ str ] = os.listdir( path = current_dir )
        debug: str = f'Listing directory contents...'
        ic( debug )
        for content in listing_dir:
            print( content )
            if self.data_path == content:
                debug: str = f'Folder { content } already exists!'
                ic( debug )
            else:
                debug: str = f'Folder { content } was not found!'
                ic( debug )
                time.sleep( 1.5 )
                info: str = f'Creating a new { self.data_path } folder in current directory...'
                ic( info )
                os.mkdir( path = self.data_path )






class DoRequestsBase( ABC ):
    def __init__(
        self,
        api: str = 'https://narutodb.xyz/api'
    ) -> None:
        self.api: str = api
        self.utils = Utils()


    @abstractmethod
    def check_status( self ) -> bool:
        return bool()


    @abstractmethod
    def connetor( self, ok: bool ) -> None:
        pass

    @abstractmethod
    def all_characters( self ) -> None:
        pass


    def process_data( self ):
        _ok: bool = self.check_status()
        self.connetor( ok = _ok)




class DoRequests( DoRequestsBase ):
    def __init__(
        self,
    ) -> None:
        self.api: str = 'https://narutodb.xyz/api'
        self.utils = Utils()

    def check_status( self ) -> bool:
        response = requests.get( url = self.api+'/character' )
        self.response = response
        debug: str
        status: int = response.status_code

        if status == 200:
            debug: str = f'Response status: { status }'
            ic( debug )
            return True
        else:
            error: str = response.text
            debug: str = f'Opss! Error while trying connect on API! Please, check the error and try again...'
            ic( debug )
            time.sleep( 1.5 )
            ic( error )
            return False



    def connetor( self, ok: bool ) -> None:
        match ok:
            case True:
                info: str = 'Great! Everything is ok!'
                debug: str = 'Getting all Naruto characters...'
                ic( info )
                time.sleep( 1.5 )
                ic( debug )
                self.all_characters()
            case False:
                exit( code = 1 )



    def all_characters( self ) -> None:
        response = requests.get( url = self.api+'/character' )
        json_response = response.json()

        self.utils.to_PolarsDataFrame( data = json_response.get( 'characters' ) )
        self.utils.convert_to_json( data = json_response.get( 'characters' ) )









if __name__ == '__main__':
    def main() -> None:
        execute = DoRequests()
        execute.process_data()

    main()