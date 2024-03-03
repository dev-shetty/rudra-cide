// Component for dragging and dropping images which will be sent to ML Model for detection
"use client"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Loader2 } from "lucide-react"
import Image from "next/image"
import { ChangeEvent, FormEvent, useState } from "react"

interface FormData {
  images: (string | ArrayBuffer | null)[]
  similar_images: boolean
}

export function ImageBox() {
  const [imageURL, setImageURL] = useState<string>()
  const [isLoading, setIsLoading] = useState(false)
  const [response, setResponse] = useState(null)
  const [error, setError] = useState<string | null>(null)

  function onImageUpload(e: ChangeEvent<HTMLInputElement>) {
    setImageURL(e.target.value)
  }

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    setIsLoading(true)
    setError(null)

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/v1/image/image-exif`,
        {
          method: "POST",
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
          body: JSON.stringify({
            img: imageURL,
          }),
        }
      )
      const data = await response.json()
      console.log(data)
      if (data.success) {
        setResponse(data)
      } else {
        setError("Cannot find the exif data")
      }
    } catch (error) {
      console.log(error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <section className="grid items-center mt-8 md:mt-4 min-h-screen">
      <div className="flex flex-col items-center justify-center space-y-4">
        <div className="mb-8">
          <h1 className="text-7xl font-bold tracking-tighter mb-8 border-foreground px-8 py-4 rounded-lg">
            Rudra-Cide
          </h1>
          <p className="-mt-12 relative -mr-12 z-1 bg-foreground/20 text-right w-fit ml-auto px-2 py-1 rounded-md border border-foreground">
            Exif Extractor
          </p>
        </div>
        <form
          encType="multipart/form-data"
          className="w-full"
          method="post"
          onSubmit={handleSubmit}
        >
          <div className="flex flex-col items-center w-full">
            <div className="relative w-1/2">
              <Input
                type="input"
                name="image"
                placeholder="Enter onion image url"
                id="image"
                onChange={onImageUpload}
                className="w-full"
                required
              />
            </div>
            <div className="mt-4">
              <Button type="submit" disabled={isLoading}>
                {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                Extract Exif Data
              </Button>
            </div>
          </div>
        </form>
        {error && <p className="text-red-500 text-center">{error}</p>}
      </div>
      {response && (
        <div className="text-center">
          {/* @ts-ignore */}
          {Object.entries(response.metadata!).map(([key, value]) => (
            <div key={key}>
              {/* @ts-ignore */}
              <strong>{key}:</strong> {value!}
            </div>
          ))}
        </div>
      )}
    </section>
  )
}
