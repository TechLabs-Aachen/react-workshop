import IconButton from '@mui/material/IconButton';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import FormControl from '@mui/material/FormControl';
import SearchIcon from '@mui/icons-material/Search';
import { useState, useEffect } from 'react';



export default function Headbar ({searchValue, setSearchValue}) {
    


    function handleSubmit(searchValue: String) {
        console.log(searchValue)
        //setSearchValue2(searchValue)
        
        // here the API fetch.. 
    }

    return ( 
        <div>
            <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
                <InputLabel htmlFor="outlined-adornment-password">Search</InputLabel>
                    <OutlinedInput
                        id="outlined-adornment-password"
                        type={ 'text' }
                        value={searchValue}
                        onChange={(event) => { setSearchValue(event.target.value) }}
                        endAdornment={
                        <InputAdornment position="end">
                            <IconButton
                            aria-label="toggle password visibility"
                            edge="end"
                            onClick = {()=> {handleSubmit(searchValue)}}>  
                            <SearchIcon></SearchIcon>               
                            </IconButton>
                        </InputAdornment>
                        }
                        label="Search"
                    />
            </FormControl>
            <div>debug var: {searchValue}</div>
        </div>
     
     );
}
 
