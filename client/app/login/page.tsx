import Loginform from '@/components/auth/Loginform'
import React from 'react'
import Image from 'next/image'
import stockImage from "@/assets/sebastian-svenson-LpbyDENbQQg-unsplash.jpg"

const login = () => {
  return (
    <div className='flex justify-between items-center'>
      <div>
        <Loginform/>
      </div>
      <div className='w-[70%] h-full items-center'>
        <Image alt='image' src={stockImage} sizes='100' className='h-full w-full  rounded-md'/>
      </div>
    </div>
  )
}

export default login