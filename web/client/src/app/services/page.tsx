import Image from "next/image"
import { default as Link, default as p } from "next/link"

export default function ServicePage() {
  return (
    <section className="container">
      <div className="text-center my-16">
        <h2 className="text-3xl font-bold leading-tight mb-4">
          Dark Web Monitoring Tool Services
        </h2>
        <p className="text-gray-400 mb-8">
          Stay ahead of threats with real-time monitoring of your digital
          footprint on the dark web.
        </p>
      </div>
      <div className="grid grid-cols-2 gap-4">
        <Link
          href="/search"
          className="grid grid-rows-4 min-h-96 rounded-md border"
        >
          <div className="relative row-span-3 overflow-hidden rounded-t-md">
            <Image
              src="/keywords.jpg"
              alt="magnifying glass searching over alphabets"
              fill
              className="w-full aspect-square transition-all duration-500 hover:scale-110 rounded-t-md"
            />
          </div>
          <div className="flex flex-col justify-center px-4 py-6">
            <p className="text-2xl font-bold leading-tight hover:text-foreground/75">
              Keyword Search
            </p>
            <p className="text-gray-400">
              Search for keywords on the dark web.
            </p>
          </div>
        </Link>
        <Link href="/finder" className="grid grid-rows-4 rounded-md border">
          <div className="relative row-span-3 overflow-hidden rounded-t-md">
            <Image
              src="/person.webp"
              alt="magnifying glass searching over alphabets"
              fill
              className="w-full aspect-square transition-all duration-500 hover:scale-110 rounded-t-md"
            />
          </div>
          <div className="flex flex-col justify-center px-4 py-6">
            <p className="text-2xl font-bold leading-tight hover:text-foreground/75">
              User Finder
            </p>
            <p className="text-gray-400">
              Find users on the dark web using keywords.
            </p>
          </div>
        </Link>
      </div>
    </section>
  )
}
