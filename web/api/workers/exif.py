import exifread

class Exif:
    def gps_to_decimal(self, degrees, minutes, seconds):
        decimal_degrees = degrees + minutes / 60 + seconds / 3600
        return decimal_degrees

    def convert_coordinates(self, latitude, longitude, latitude_dir, longitude_dir):
        latitude_decimal = self.gps_to_decimal(latitude[0], latitude[1], latitude[2])
        if latitude_dir == 'S':
            latitude_decimal *= -1
        longitude_decimal = self.gps_to_decimal(longitude[0], longitude[1], longitude[2])
        if longitude_dir == 'W':
            longitude_decimal *= -1
        return eval(str(latitude_decimal)), eval(str(longitude_decimal))

    def timeStamp(self, timestamp):
        hours, minutes, seconds_fraction = timestamp
        seconds = int(seconds_fraction * 100)
        output = "{0}:{1}:{2}".format(int(hours), int(minutes), int(seconds/100))
        return output

    async def extract_metadata(self, image_path):
        try:
            with open(image_path, 'rb') as image_file:
                tags = exifread.process_file(image_file)
                metadata = {}
                for tag in tags.keys():
                    if tag.startswith('GPS'):
                        metadata[tag] = tags[tag]
                    elif tag.startswith('Image'):
                        metadata[tag] = tags[tag]
                if 'GPS GPSLatitude' in metadata and 'GPS GPSLongitude' in metadata:
                    latitude = metadata['GPS GPSLatitude'].values
                    longitude = metadata['GPS GPSLongitude'].values
                    latitude_dir = metadata['GPS GPSLatitudeRef'].values
                    longitude_dir = metadata['GPS GPSLongitudeRef'].values
                    metadata['GPS GPSTimeStamp'] = self.timeStamp(metadata['GPS GPSTimeStamp'].values)
                    metadata['GPS GPSLatitude'], metadata['GPS GPSLongitude'] = self.convert_coordinates(latitude, longitude, latitude_dir, longitude_dir)
                return {'success': True, "metadata": metadata }
            return {'success': False, 'message': 'Unable to get the image.'}
        except Exception:
            return {'success': False, 'message': 'Error extracting metadata from the image.'}

# if __name__ == "__main__":
#     image_path = input("Enter the path to the image file: ")
#     exif = Exif()
#     metadata = exif.extract_metadata(image_path)
#     if metadata:
#         print("Metadata extracted from the image:")
#         for tag, value in metadata.items():
#             if tag == "metadata":
#                 for tag, value in value.items():
#                     print(f"{tag}: {value}")
#             else:
#                 print(f"{tag}: {value}")
#     else:
#         print("No metadata found in the image.")
