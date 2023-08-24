# ComfyMath

Provides Math Nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Features

Provides nodes for:
* Boolean Logic
* Integer Arithmetic
* Floating Point Arithmetic and Functions
* Vec2, Vec3, and Vec4 Arithmetic and Functions
* Vector Database (Qdrant)

## Installation

### Easy

ComfyMath can be installed using [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

### Manual

From the `custom_nodes` directory in your ComfyUI installation, with your venv activated, run:

```sh
git clone https://github.com/evanspearman/ComfyMath.git
cd ComfyMath
pip install -r requirements.txt
```

## Nodes

### Boolean Logic

#### BooleanUnaryOperation

Perform an operation on a single boolean value. Supported operations are:

* Not

#### BooleanBinaryOperation

Perform an operation on two boolean values. Supported operations are:

* Nor
* Xor
* Nand
* And
* Xnor
* Or
* Eq
* Neq

### Integer Arithmetic and Logic

#### IntUnaryOperation

Perform an operation on a sigle integer value. Supported operations are:

* Abs
* Neg
* Inc
* Dec
* Sqr
* Cube
* Not
* Factorial

#### IntUnaryCondition

Perform a comparison on a single integer value. Supported conditions are:

* IsZero
* IsNonZero
* IsPositive
* IsNegative
* IsEven
* IsOdd


#### IntBinaryOperation

Perform an operation on two integer values. Supported operations are:

* Add
* Sub
* Mul
* Div
* Mod
* Pow
* And
* Nand
* Or
* Nor
* Xor
* Xnor
* Shl
* Shr
* Max
* Min

#### IntBinaryCondition

Perform a comparison on two integer values. Supported conditions are:

* Eq
* Neq
* Gt
* Lt
* Geq
* Leq


### Floating Point Math

#### FloatUnaryOperation

Perform an operation on a single floating point value. Supported operations are:

* Neg
* Inc
* Dec
* Abs
* Sqr
* Cube
* Sqrt
* Exp
* Ln
* Log10
* Log2
* Sin
* Cos
* Tan
* Asin
* Acos
* Atan
* Sinh
* Cosh
* Tanh
* Asinh
* Acosh
* Atanh
* Round
* Floor
* Ceil
* Trunc
* Erf
* Erfc
* Gamma
* Radians
* Degrees

#### FloatUnaryCondition

Perform a comparison on a single floating point value. Supported conditions are:

* IsZero
* IsPositive
* IsNegative
* IsNonZero
* IsPositiveInfinity
* IsNegativeInfinity
* IsNaN
* IsFinite
* IsInfinite
* IsEven
* IsOdd

#### FloatBinaryOperation

Perform an operation on two floating point values. Supported operations are:

* Add
* Sub
* Mul
* Div
* Mod
* Pow
* FloorDiv
* Max
* Min
* Log
* Atan2

#### FloatBinaryCondition

Perform a comparison on two floating point values. Supported conditions are:

* Eq
* Neq
* Gt
* Gte
* Lt
* Lte

### Number Math

`NUMBER` is a type found in some custom nodes that can be either an `int` or a `float`.

#### NumberUnaryOperation

Same operations as FloatUnaryOperation

#### NumberUnaryCondition

Same conditions as FloatUnaryCondition

#### NumberBinaryOperation

Same conditions as FloatBinaryOperation

#### NumberBinaryCondition

Same conditions as FloatBinaryCondition

### Vector Math

Nodes for performing vector math operations in Euclidean 2-space, 3-space, and 4-space. Under the hood, the `VEC2`, `VEC3`, and `VEC4` types are implemented as `tuple[float, float]`, `tuple[float, float, float]`, and `tuple[float, float, float, float]` respectively. Each size of vector has it's own set of nodes, but the nodes have all the same operations and conditions. The actual processing is performed using numpy.

#### VecNUnaryOperation

Perform an operation on a single vector. Available operations are:

* Neg
* Normalize

#### VecNUnaryCondition

Perform a comparison on a single vector. Available conditions are:

* IsZero
* IsNotZero
* IsNormalized
* IsNotNormalized

#### VecNToScalarUnaryOperation

Perform an operation on a single vector that results in a scalar. Available operations are:

* Norm

#### VecNBinaryOperation

Perform an operation on two vectors. Available operations are:

* Add
* Sub
* Cross

#### VecNBinaryCondition

Perform a comparision on two vectors. Available conditions are:

* Eq
* Neq

#### VecNToScalarBinaryOperation

Perform an operation on two vectors that results in a scalar. Available operations are:

* Dot
* Distance

#### VecNScalarOperation

Perform an operation on a vector and a scalar. Available operations are:

* Mul
* Div

### Type Conversion

Nodes to convert between different types.

#### BoolToInt

`True` is converted to `1` and `False` is converted to `0`

#### IntToBool

`0` is converted to `False` and Non-zero is converted to `True`

#### FloatToInt

#### IntToFloat

#### IntToNumber

#### NumberToInt

#### FloatToNumber

#### NumberToFloat

#### ComposeVecN

Build a vector by composing floating point values

#### FillVecN

Build a vector by repeating a single floating point value

#### BreakoutVecN

Retrieve the floating point values that make up a vector

### Graphics

#### SDXLResolution

Allows for selecting one of the officially supported resolutions of SDXL-based models and outputs the width and height.

#### NearestSDXLResolution

Given an `IMAGE` find the SDXL resolution that has the closest aspect ratio. This is useful for Image to Image or ControlNet workflows where you want the image to have as close as possible an aspect ratio to the original image.

### Data Structures

Utilities for working with different data structures such as lists and dictionaries.

#### AddStringToDict

If no value is provided for `input_dict`, create a new dictionary and set the value of key `key` to `value.

If `input_dict` is provided, add or override the value of key `key` to `value`.

#### RetrieveStringFromDict

Give a key and existing dictionary with string keys, retrieve the value of key `key`. If the value is not a `STRING` or there is no such key, an error will occur.

#### StringAtIndex

Given a list of `STRING`, retrieve the value at the given index. 

#### FloatAtIndex

Given a list of `FLOAT`, retrieve the value at the given index.

### Image Files

Nodes for dealing with image files on disk.

#### LoadImageFromPath

Given a `STRING` representing the path to an image file on the local file system, load the image as an `IMAGE`.

#### GetImageSequence

Given a `STRING` representing the path to an image file on the local file system, return a list of paths (including the given path) where the last block of digits in the file name contains the _only_ differences compared to the given file. For instance, `image_1000.png` and `image_0210.png` would be considered part of the same sequence. `image_100_1000.png` and `image_200_1001.png` would not. `image_1000.png` and `render_1001.png` would also not. Note that this node does not try to load the images into memory or validate that they are image files.

### Vector Databases

Nodes for interacting with the vector database Qdrant. Vector databases allow indexing data on vectors, including large vectors such as embeddings. They are useful for searching for data that is "near" a given vector. This is useful for looking for semantically similar text, or images that are visually similar or contain similar subjects.

#### QdrantConnectionFromFile

Either opens or creates a connection to a Qdrant database at a given path.

#### QdrantCollection

Either creates or references an existing collection in the connected Qdrant database. The `vector_size` and `distance` inputs are optional and are only used when creating a new collection. Otherwise they are ignored. All vectors inserted into the collection must be of size `vector_size`. For CLIP, this size should be 1280 because a CLIP embedding has 1280 dimensions. `distance` sets the type of distance calculation that is used for searching the collection to determine how far apart a given vector is from the vector used as the search query. `Cosine` refers to consine similarity, `Euclid` refers to the euclidean distance, and `Dot` is the dot product.

#### CLIPVisionOutputToQdrantVector

This node is used to convert a `CLIP_VISION_OUTPUT` value into a format that can be inserted into a Qdrant collection.


#### ConditioningToQdrantVector

This node is used to convert a `CONDITIONING` value into a format that can be inserted into a Qdrant collection.

#### QdrantInsertVector

Insert a given vector into a given Qdrant collection. Optionally include a `DICT` as a payload. The id (a `STRING` representing a UUID) is output, which can be used to retrieve the inserted entry from the collection. The payload is other data that is associated with the vector. For instance, the original text that the vector is an embedding of, or the path to an image that the vector is an embedding of. This node functions as an output node so no other output node needs to exist in the workflow in order to execute it.

#### QdrantRetrievePayloadById

Given an id, get the payload from the given qdrant collection that is associated with that id. This is useful after performing a search as the QdrantSearch node does not retrieve the payloads of similar vectors it found. Only the associated ids.

#### QdrantSearch

Given a vector search for nearby vectors in the given collection. The limit value is the maximum number of entries to output. This node does not output the vectors or payloads of the nearby vectors, rather, it outputs a list of ids associated with those vectors in the collection and a list of scores that represent how close the vector associated with the id at the same index in the lists is to the original vector. Use the QdrantRetrievePayloadById node to retrieve the payload associated with the output ids.

#### QdrantInsertImageSequence

Given an image sequence (list of paths to image files) and a CLIP Vision Model, encode the images using the CLIP Vision model and insert the embedding into the given collection. Each embedding will be inserted with a payload of `{"path": "/path/to/image"}`. This node functions as an output node so no other output node needs to exist in the workflow in order to execute it.
