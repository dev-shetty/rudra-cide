import { Button } from "@/components/ui/button"
import { ArrowRight } from "lucide-react"
import Image from "next/image"
import Link from "next/link"

export default function Component() {
  return (
    <div className="grid min-h-screen bg-background/30">
      <section className="grid grid-cols-2 items-center justify-between">
        <div className="relative flex items-center justify-center w-full h-full bg-background/80 px-8 py-16 rounded-md">
          <div className="max-w-lg">
            <h2 className="text-6xl font-bold leading-tight mb-4">
              Dark Web Monitoring Tool
            </h2>
            <p className="text-gray-400 mb-8">
              Stay ahead of threats with real-time monitoring of your digital
              footprint on the dark web.
            </p>
            <Button className="flex gap-1" asChild>
              <Link href="/services" className="w-fit">
                Explore services <ArrowRight className="scale-75" />
              </Link>
            </Button>
          </div>
        </div>
        <div className="w-full h-full -z-10 rounded-full flex items-center justify-center">
          <Image
            quality={100}
            alt="Placeholder"
            fill
            src="/matrix.avif"
            className="object-cover mix-blend-hard-light"
          />
        </div>
      </section>
    </div>
  )
}
