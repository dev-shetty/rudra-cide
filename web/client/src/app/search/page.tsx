"use client"

import Keywords from "@/components/keywords"
import Search from "@/components/search"
import { useState } from "react"

export default function SearchPage() {
  const [inputs, setInputs] = useState<string[]>([""])

  return (
    <section className="grid mx-auto min-h-screen items-center px-4 md:px-6 py-6 md:py-12 w-1/2">
      <div className="flex flex-col items-center justify-center space-y-4">
        <div className="mb-8">
          <h1 className="text-7xl font-bold tracking-tighter mb-8 border-foreground px-8 py-4 rounded-lg">
            Rudra-Cide
          </h1>
          <p className="-mt-12 relative -mr-12 z-1 bg-foreground/20 text-right w-fit ml-auto px-2 py-1 rounded-md border border-foreground">
            Keywords Search
          </p>
        </div>
        <div className="grid gap-12">
          <Search inputs={inputs} />
          <div className="flex flex-col gap-4">
            <p className="text-center">- Add Keywords to filter - </p>
            <Keywords inputs={inputs} setInputs={setInputs} />
          </div>
        </div>
      </div>
    </section>
  )
}
