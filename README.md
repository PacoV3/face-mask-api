# face-mask-api

PENDING.

## Implementation

In order to use the API with docker the first step is to build the image with the next command, executing it from the code folder.

```bash
docker build -t [name_for_image] .
```

Then use the image with this last command.

```bash
docker run --rm -v [project_route]:/app -p 5001:5001 [name_for_image]
```

## Usage

For examples on how to use the app, here is a way to test it with [curl](https://curl.se/docs/manpage.html) (you'll need to have the files in the route you are executing it).

For a single file in /examples:

```bash
curl -X POST -F files=@'mask4.jpg' http://127.0.0.1:5001/thermal_model
```

For multiple files in /examples:

```bash
curl -X POST -F files=@'mask4.jpg' -F files=@'mask5.jpg' -F files=@'mask1.jpg' -F files=@'no_mask1.jpg' http://127.0.0.1:5001/thermal_model
```