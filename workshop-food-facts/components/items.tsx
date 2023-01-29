import ListItemText from '@mui/material/ListItemText';
import ListItemButton from '@mui/material/ListItemButton';
import List from '@mui/material/List';
import style from '../styles/Items.module.css'
import { useState } from 'react';



export default function Items(props: { data: any; }) {

    const [data, setdata] = useState(props.data)
   // console.log(props.data)
    const showItems = () => {
        var item = []
        for (let i = 0; i < data.length; i++) {

            item.push(

                <ListItemButton component="a" href="#simple-list"  >
                    <div className={style.card}>

                        <img src={data[i].Url}></img>
                        <div className={style.nameQuantity}>
                            <ListItemText primary={data[i].name} />
                            <ListItemText primary={data[i].quantity} />
                        </div>
                    </div>
                </ListItemButton>

            )

        }
        return item

    }


    return (
        <div className={style.cards}>
            {showItems()}
        </div>

    )

}