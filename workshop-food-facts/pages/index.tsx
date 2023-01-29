import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import MenuIcon from '@mui/icons-material/Menu';
import { useState, useEffect } from 'react';
import Items from '@/components/items'
import Headbar from '../components/Headbar'



export default function Home() {
  const [searchValue, setSearchValue] = useState("ab")
  const mockData = [
      { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Nutella', quantity: '400g' },
      { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Banane', quantity: '1kg' },
      { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Dead', quantity: '0g' }
    ]
 

    
  return (
    <div>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <IconButton size="large" edge="start" color="inherit" aria-label="open drawer" sx={{ mr: 2 }}>
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" noWrap component="div" sx={{ display: { xs: 'none', sm: 'block' } }}>
              MUI
            </Typography>
            <Headbar searchValue={searchValue} setSearchValue={setSearchValue} ></Headbar>   
            <div>Debug var: {searchValue}</div>            
          </Toolbar>
        </AppBar>                
      </Box>      
      <Items data={mockData}></Items>
    </div>    
  );
}


