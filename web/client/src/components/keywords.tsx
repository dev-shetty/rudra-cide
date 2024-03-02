"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { PlusCircle, X } from "lucide-react"
import { Dispatch, SetStateAction, useState } from "react"

type KeywordsProps = {
  inputs: string[]
  setInputs: Dispatch<SetStateAction<string[]>>
}

export default function Keywords({ inputs, setInputs }: KeywordsProps) {
  function addInput() {
    const newInputs = [...inputs, ""]
    setInputs(newInputs)
  }

  function removeInput(index: number) {
    setInputs((prev) => {
      const newInputs = [...prev]
      newInputs.splice(index, 1)
      return newInputs
    })
  }

  return (
    <div className="flex flex-col">
      <div className="grid grid-cols-4 gap-1">
        {inputs.map((inp, index) => (
          <div key={index} className="flex items-center relative mb-4">
            <Input
              type="text"
              placeholder="Keyword"
              onChange={(e) => {
                const text = e.target.value
                const newInputs = [...inputs]
                newInputs[index] = text
                setInputs(newInputs)
              }}
            />
            <X
              onClick={() => removeInput(index)}
              className="absolute right-2 cursor-pointer"
            />
          </div>
        ))}
      </div>
      <Button onClick={addInput} className="flex gap-2">
        Add Keyword
        <PlusCircle />
      </Button>
    </div>
  )
}
