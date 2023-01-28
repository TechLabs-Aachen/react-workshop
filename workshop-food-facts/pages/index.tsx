import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import Items from '@/components/items'


const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const mockData = [
    { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Nutella', quantity: '400g' },
    { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Banane', quantity: '1kg' },
    { Url: 'https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.676.200.jpg', name: 'Dead', quantity: '0g' }
  ]
  return (

    <Items data={mockData}></Items>
  )
}
