import Loginform from '@/components/auth/Loginform'
import React from 'react'
import Image from 'next/image'
import stockImage from "@/assets/images/sebastian-svenson-LpbyDENbQQg-unsplash.jpg"

const login = () => {
  return (
 <div className='flex lg:justify-between gap-10 my-10 lg:my-0  min-h-screen lg:items-center justify-center items-center'>
      <div className="w-100">
        <Loginform/>
      </div>
      <div className='relative hidden w-150 h-150 lg:block overflow-hidden'>
        <Image alt='image' src={stockImage} fill className='w-full h-full object-cover rounded-md'/>
      </div>
    </div>
  )
}

export default login