{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "758eb4b1",
   "metadata": {},
   "source": [
    "#1. Import the NUMPY package under the name np."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e2d6b6c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb76893f",
   "metadata": {},
   "source": [
    "2. Print the NUMPY version and the configuration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9a16839d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.20.2\n"
     ]
    }
   ],
   "source": [
    "print(np.version.version)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d78f8852",
   "metadata": {},
   "source": [
    "3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable \"a\"\n",
    "Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0e6e1978",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.random.random((2, 3, 5))\n",
    "x = np.random.rand(2,3,2)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8345a5f0",
   "metadata": {},
   "source": [
    "4. Print a."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "335162e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.38183948 0.37068604 0.3847485  0.04762216 0.27991861]\n",
      "  [0.48510236 0.83562852 0.04317602 0.14154871 0.55054592]\n",
      "  [0.49718255 0.64505409 0.24472004 0.8523841  0.20450765]]\n",
      "\n",
      " [[0.36829737 0.36323891 0.71537105 0.50286103 0.89102422]\n",
      "  [0.54170106 0.37229036 0.13805319 0.11002754 0.00220201]\n",
      "  [0.83092529 0.85229272 0.23757892 0.70523489 0.56789702]]]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2ad3c49",
   "metadata": {},
   "source": [
    "5. Create a 5x2x3 3-dimensional array with all values equaling 1.\n",
    "#Assign the array to variable \"b\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f2a4e781",
   "metadata": {},
   "outputs": [],
   "source": [
    "b=np.ones((5,2,3))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "717aca3d",
   "metadata": {},
   "source": [
    "6. Print b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bd4df7bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]]\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ad6f039",
   "metadata": {},
   "source": [
    "7. Do a and b have the same size? How do you prove that in Python code?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c63dbe14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "print(np.size(a))\n",
    "print(np.size(b))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbc1e3b0",
   "metadata": {},
   "source": [
    "8. Are you able to add a and b? Why or why not?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44e6065e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Nop, because they don't have the same shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e6ebf81",
   "metadata": {},
   "source": [
    "9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe \"c\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "44b40954",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3, 5)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c= b.transpose(1,2,0)\n",
    "np.shape(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b4f6954",
   "metadata": {},
   "source": [
    "10. Try to add a and c. Now it should work. Assign the sum to varialbe \"d\". But why does it work now?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "dd052a01",
   "metadata": {},
   "outputs": [],
   "source": [
    "d =a + c"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33ba110c",
   "metadata": {},
   "source": [
    "11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "8c41e555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1.00610845 1.7694044  1.11208872 1.91581605 1.95771213]\n",
      "  [1.38085648 1.25888415 1.06223416 1.69259286 1.01159255]\n",
      "  [1.85170116 1.0555312  1.47709779 1.54899818 1.10878724]]\n",
      "\n",
      " [[1.4081789  1.89892526 1.7806715  1.99547819 1.12157533]\n",
      "  [1.99910876 1.24408407 1.55260699 1.89079419 1.49043039]\n",
      "  [1.46158208 1.07566442 1.26319237 1.98041121 1.2284756 ]]]\n",
      "1.006108450640372\n"
     ]
    }
   ],
   "source": [
    "print(d)\n",
    "print(d[0][0][0])\n",
    "#each element of the array consist of tht sum of the same element of the to preciding ones"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aec9f722",
   "metadata": {},
   "source": [
    "12. Multiply a and c. Assign the result to e."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "bbae3db3",
   "metadata": {},
   "outputs": [],
   "source": [
    "e = a * c"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b013d5d6",
   "metadata": {},
   "source": [
    "13. Does e equal to a? Why or why not?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3e7fba8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(a is e) # tienen dimensiones (filas de la primera y columnas de la segunda) diferentes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6241b81",
   "metadata": {},
   "source": [
    "14. Identify the max, min, and mean values in d. Assign those values to variables \"d_max\", \"d_min\", and \"d_mean\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "7b14812a",
   "metadata": {},
   "outputs": [],
   "source": [
    "d_max=np.max(d)\n",
    "d_min=np.min(d)\n",
    "d_mean=np.mean(d)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c49b545a",
   "metadata": {},
   "source": [
    "15. Now we want to label the values in d. First create an empty array \"f\" with the same shape (i.e. 2x3x5) \n",
    "as d using `np.empty`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9d0a6a4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<built-in function empty>\n"
     ]
    }
   ],
   "source": [
    "f = np.empty((2,3,5))\n",
    "print(np.empty)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77a9d6fb",
   "metadata": {},
   "source": [
    "16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.\n",
    "If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.\n",
    "If a value equals to d_mean, assign 50 to the corresponding value in f.\n",
    "Assign 0 to the corresponding value(s) in f for d_min in d.\n",
    "Assign 100 to the corresponding value(s) in f for d_max in d.\n",
    "In the end, f should have only the following values: 0, 25, 50, 75, and 100.\n",
    "Note: you don't have to use Numpy in this question."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "54a64d97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1.00610845 75.         25.         75.         75.        ]\n",
      "  [25.         25.         25.         75.         25.        ]\n",
      "  [75.         25.         25.         75.         25.        ]]\n",
      "\n",
      " [[25.         75.         75.         75.         25.        ]\n",
      "  [ 0.         25.         75.         75.         75.        ]\n",
      "  [25.         25.         25.         75.         25.        ]]]\n"
     ]
    }
   ],
   "source": [
    "for i in range(2):\n",
    "    for j in range(3):\n",
    "        for k in range(5):\n",
    "            if (d[i][j][k] > d_min) & (d[i][j][k] < d_mean):\n",
    "                f[i, j , k] = 25\n",
    "            elif (d[i][j][k] < d_max) & (d[i][j][k] > d_mean):\n",
    "                f[i, j , k] = 75\n",
    "            elif d[i][j][k] == d_mean:\n",
    "                f[i, j , k] = 50\n",
    "            elif d[i][j][k] > d_max:\n",
    "                f[i, j , k] = 100\n",
    "            elif d[i][j][k] > d_min:\n",
    "                f[i, j , k] = 0\n",
    "print (f)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03cbf91c",
   "metadata": {},
   "source": [
    "17. Print d and f. Do you have your expected f?\n",
    "For instance, if your d is:\n",
    "array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],\n",
    "        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],\n",
    "        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],\n",
    "\n",
    "       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],\n",
    "        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],\n",
    "        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])\n",
    "\n",
    "Your f should be:\n",
    "array([[[ 75.,  75.,  75.,  25.,  75.],\n",
    "        [ 75.,  75.,  25.,  25.,  25.],\n",
    "        [ 75.,  25.,  75.,  75.,  75.]],\n",
    "\n",
    "       [[ 25.,  25.,  25.,  25., 100.],\n",
    "        [ 75.,  75.,  75.,  75.,  75.],\n",
    "        [ 25.,  75.,   0.,  75.,  75.]]])\n",
    "\"\"\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "76c0e05e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1.00610845 1.7694044  1.11208872 1.91581605 1.95771213]\n",
      "  [1.38085648 1.25888415 1.06223416 1.69259286 1.01159255]\n",
      "  [1.85170116 1.0555312  1.47709779 1.54899818 1.10878724]]\n",
      "\n",
      " [[1.4081789  1.89892526 1.7806715  1.99547819 1.12157533]\n",
      "  [1.99910876 1.24408407 1.55260699 1.89079419 1.49043039]\n",
      "  [1.46158208 1.07566442 1.26319237 1.98041121 1.2284756 ]]]\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10162058",
   "metadata": {},
   "source": [
    "18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values \n",
    "(\"A\", \"B\", \"C\", \"D\", and \"E\") to label the array elements? You are expecting the result to be:\n",
    "array([[[ 'D',  'D',  'D',  'B',  'D'],\n",
    "        [ 'D',  'D',  'B',  'B',  'B'],\n",
    "        [ 'D',  'B',  'D',  'D',  'D']],\n",
    "\n",
    "       [[ 'B',  'B',  'B',  'B',  'E'],\n",
    "        [ 'D',  'D',  'D',  'D',  'D'],\n",
    "        [ 'B',  'D',   'A',  'D', 'D']]])\n",
    "Again, you don't need Numpy in this question."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "61e43d0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[['(1.006108450640372+0j)' 'D' 'B' 'D' 'D']\n",
      "  ['B' 'B' 'B' 'D' 'B']\n",
      "  ['D' 'B' 'B' 'D' 'B']]\n",
      "\n",
      " [['B' 'D' 'D' 'D' 'B']\n",
      "  ['A' 'B' 'D' 'D' 'D']\n",
      "  ['B' 'B' 'B' 'D' 'B']]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "f= f.astype(str)\n",
    "for i in range(2):\n",
    "    for j in range(3):\n",
    "        for k in range(5):\n",
    "            if (d[i][j][k] > d_min) & (d[i][j][k] < d_mean):\n",
    "                f[i, j , k] = \"B\"\n",
    "            elif (d[i][j][k] < d_max) & (d[i][j][k] > d_mean):\n",
    "                f[i, j , k] = \"D\"\n",
    "            elif d[i][j][k] == d_mean:\n",
    "                f[i, j , k] = \"C\"\n",
    "            elif d[i][j][k] > d_max:\n",
    "                f[i, j , k] = \"E\"\n",
    "            elif d[i][j][k] > d_min:\n",
    "                f[i, j , k] = \"A\"\n",
    "print (f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "b221f4b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on class dtype in module numpy:\n",
      "\n",
      "class dtype(builtins.object)\n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __bool__(self, /)\n",
      " |      self != 0\n",
      " |  \n",
      " |  __eq__(self, value, /)\n",
      " |      Return self==value.\n",
      " |  \n",
      " |  __ge__(self, value, /)\n",
      " |      Return self>=value.\n",
      " |  \n",
      " |  __getitem__(self, key, /)\n",
      " |      Return self[key].\n",
      " |  \n",
      " |  __gt__(self, value, /)\n",
      " |      Return self>value.\n",
      " |  \n",
      " |  __hash__(self, /)\n",
      " |      Return hash(self).\n",
      " |  \n",
      " |  __le__(self, value, /)\n",
      " |      Return self<=value.\n",
      " |  \n",
      " |  __len__(self, /)\n",
      " |      Return len(self).\n",
      " |  \n",
      " |  __lt__(self, value, /)\n",
      " |      Return self<value.\n",
      " |  \n",
      " |  __mul__(self, value, /)\n",
      " |      Return self*value.\n",
      " |  \n",
      " |  __ne__(self, value, /)\n",
      " |      Return self!=value.\n",
      " |  \n",
      " |  __reduce__(...)\n",
      " |      Helper for pickle.\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  __rmul__(self, value, /)\n",
      " |      Return value*self.\n",
      " |  \n",
      " |  __setstate__(...)\n",
      " |  \n",
      " |  __str__(self, /)\n",
      " |      Return str(self).\n",
      " |  \n",
      " |  newbyteorder(...)\n",
      " |      newbyteorder(new_order='S', /)\n",
      " |      \n",
      " |      Return a new dtype with a different byte order.\n",
      " |      \n",
      " |      Changes are also made in all fields and sub-arrays of the data type.\n",
      " |      \n",
      " |      Parameters\n",
      " |      ----------\n",
      " |      new_order : string, optional\n",
      " |          Byte order to force; a value from the byte order specifications\n",
      " |          below.  The default value ('S') results in swapping the current\n",
      " |          byte order.  `new_order` codes can be any of:\n",
      " |      \n",
      " |          * 'S' - swap dtype from current to opposite endian\n",
      " |          * {'<', 'little'} - little endian\n",
      " |          * {'>', 'big'} - big endian\n",
      " |          * '=' - native order\n",
      " |          * {'|', 'I'} - ignore (no change to byte order)\n",
      " |      \n",
      " |      Returns\n",
      " |      -------\n",
      " |      new_dtype : dtype\n",
      " |          New dtype object with the given change to the byte order.\n",
      " |      \n",
      " |      Notes\n",
      " |      -----\n",
      " |      Changes are also made in all fields and sub-arrays of the data type.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> import sys\n",
      " |      >>> sys_is_le = sys.byteorder == 'little'\n",
      " |      >>> native_code = sys_is_le and '<' or '>'\n",
      " |      >>> swapped_code = sys_is_le and '>' or '<'\n",
      " |      >>> native_dt = np.dtype(native_code+'i2')\n",
      " |      >>> swapped_dt = np.dtype(swapped_code+'i2')\n",
      " |      >>> native_dt.newbyteorder('S') == swapped_dt\n",
      " |      True\n",
      " |      >>> native_dt.newbyteorder() == swapped_dt\n",
      " |      True\n",
      " |      >>> native_dt == swapped_dt.newbyteorder('S')\n",
      " |      True\n",
      " |      >>> native_dt == swapped_dt.newbyteorder('=')\n",
      " |      True\n",
      " |      >>> native_dt == swapped_dt.newbyteorder('N')\n",
      " |      True\n",
      " |      >>> native_dt == native_dt.newbyteorder('|')\n",
      " |      True\n",
      " |      >>> np.dtype('<i2') == native_dt.newbyteorder('<')\n",
      " |      True\n",
      " |      >>> np.dtype('<i2') == native_dt.newbyteorder('L')\n",
      " |      True\n",
      " |      >>> np.dtype('>i2') == native_dt.newbyteorder('>')\n",
      " |      True\n",
      " |      >>> np.dtype('>i2') == native_dt.newbyteorder('B')\n",
      " |      True\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from numpy._DTypeMeta\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Data descriptors defined here:\n",
      " |  \n",
      " |  alignment\n",
      " |      The required alignment (bytes) of this data-type according to the compiler.\n",
      " |      \n",
      " |      More information is available in the C-API section of the manual.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> x = np.dtype('i4')\n",
      " |      >>> x.alignment\n",
      " |      4\n",
      " |      \n",
      " |      >>> x = np.dtype(float)\n",
      " |      >>> x.alignment\n",
      " |      8\n",
      " |  \n",
      " |  base\n",
      " |      Returns dtype for the base element of the subarrays,\n",
      " |      regardless of their dimension or shape.\n",
      " |      \n",
      " |      See Also\n",
      " |      --------\n",
      " |      dtype.subdtype\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> x = numpy.dtype('8f')\n",
      " |      >>> x.base\n",
      " |      dtype('float32')\n",
      " |      \n",
      " |      >>> x =  numpy.dtype('i2')\n",
      " |      >>> x.base\n",
      " |      dtype('int16')\n",
      " |  \n",
      " |  byteorder\n",
      " |      A character indicating the byte-order of this data-type object.\n",
      " |      \n",
      " |      One of:\n",
      " |      \n",
      " |      ===  ==============\n",
      " |      '='  native\n",
      " |      '<'  little-endian\n",
      " |      '>'  big-endian\n",
      " |      '|'  not applicable\n",
      " |      ===  ==============\n",
      " |      \n",
      " |      All built-in data-type objects have byteorder either '=' or '|'.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> dt = np.dtype('i2')\n",
      " |      >>> dt.byteorder\n",
      " |      '='\n",
      " |      >>> # endian is not relevant for 8 bit numbers\n",
      " |      >>> np.dtype('i1').byteorder\n",
      " |      '|'\n",
      " |      >>> # or ASCII strings\n",
      " |      >>> np.dtype('S2').byteorder\n",
      " |      '|'\n",
      " |      >>> # Even if specific code is given, and it is native\n",
      " |      >>> # '=' is the byteorder\n",
      " |      >>> import sys\n",
      " |      >>> sys_is_le = sys.byteorder == 'little'\n",
      " |      >>> native_code = sys_is_le and '<' or '>'\n",
      " |      >>> swapped_code = sys_is_le and '>' or '<'\n",
      " |      >>> dt = np.dtype(native_code + 'i2')\n",
      " |      >>> dt.byteorder\n",
      " |      '='\n",
      " |      >>> # Swapped code shows up as itself\n",
      " |      >>> dt = np.dtype(swapped_code + 'i2')\n",
      " |      >>> dt.byteorder == swapped_code\n",
      " |      True\n",
      " |  \n",
      " |  char\n",
      " |      A unique character code for each of the 21 different built-in types.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> x = np.dtype(float)\n",
      " |      >>> x.char\n",
      " |      'd'\n",
      " |  \n",
      " |  descr\n",
      " |      `__array_interface__` description of the data-type.\n",
      " |      \n",
      " |      The format is that required by the 'descr' key in the\n",
      " |      `__array_interface__` attribute.\n",
      " |      \n",
      " |      Warning: This attribute exists specifically for `__array_interface__`,\n",
      " |      and passing it directly to `np.dtype` will not accurately reconstruct\n",
      " |      some dtypes (e.g., scalar and subarray dtypes).\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> x = np.dtype(float)\n",
      " |      >>> x.descr\n",
      " |      [('', '<f8')]\n",
      " |      \n",
      " |      >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n",
      " |      >>> dt.descr\n",
      " |      [('name', '<U16'), ('grades', '<f8', (2,))]\n",
      " |  \n",
      " |  fields\n",
      " |      Dictionary of named fields defined for this data type, or ``None``.\n",
      " |      \n",
      " |      The dictionary is indexed by keys that are the names of the fields.\n",
      " |      Each entry in the dictionary is a tuple fully describing the field::\n",
      " |      \n",
      " |        (dtype, offset[, title])\n",
      " |      \n",
      " |      Offset is limited to C int, which is signed and usually 32 bits.\n",
      " |      If present, the optional title can be any object (if it is a string\n",
      " |      or unicode then it will also be a key in the fields dictionary,\n",
      " |      otherwise it's meta-data). Notice also that the first two elements\n",
      " |      of the tuple can be passed directly as arguments to the ``ndarray.getfield``\n",
      " |      and ``ndarray.setfield`` methods.\n",
      " |      \n",
      " |      See Also\n",
      " |      --------\n",
      " |      ndarray.getfield, ndarray.setfield\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n",
      " |      >>> print(dt.fields)\n",
      " |      {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}\n",
      " |  \n",
      " |  flags\n",
      " |      Bit-flags describing how this data type is to be interpreted.\n",
      " |      \n",
      " |      Bit-masks are in `numpy.core.multiarray` as the constants\n",
      " |      `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,\n",
      " |      `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation\n",
      " |      of these flags is in C-API documentation; they are largely useful\n",
      " |      for user-defined data-types.\n",
      " |      \n",
      " |      The following example demonstrates that operations on this particular\n",
      " |      dtype requires Python C-API.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> x = np.dtype([('a', np.int32, 8), ('b', np.float64, 6)])\n",
      " |      >>> x.flags\n",
      " |      16\n",
      " |      >>> np.core.multiarray.NEEDS_PYAPI\n",
      " |      16\n",
      " |  \n",
      " |  hasobject\n",
      " |      Boolean indicating whether this dtype contains any reference-counted\n",
      " |      objects in any fields or sub-dtypes.\n",
      " |      \n",
      " |      Recall that what is actually in the ndarray memory representing\n",
      " |      the Python object is the memory address of that object (a pointer).\n",
      " |      Special handling may be required, and this attribute is useful for\n",
      " |      distinguishing data types that may contain arbitrary Python objects\n",
      " |      and data-types that won't.\n",
      " |  \n",
      " |  isalignedstruct\n",
      " |      Boolean indicating whether the dtype is a struct which maintains\n",
      " |      field alignment. This flag is sticky, so when combining multiple\n",
      " |      structs together, it is preserved and produces new dtypes which\n",
      " |      are also aligned.\n",
      " |  \n",
      " |  isbuiltin\n",
      " |      Integer indicating how this dtype relates to the built-in dtypes.\n",
      " |      \n",
      " |      Read-only.\n",
      " |      \n",
      " |      =  ========================================================================\n",
      " |      0  if this is a structured array type, with fields\n",
      " |      1  if this is a dtype compiled into numpy (such as ints, floats etc)\n",
      " |      2  if the dtype is for a user-defined numpy type\n",
      " |         A user-defined type uses the numpy C-API machinery to extend\n",
      " |         numpy to handle a new array type. See\n",
      " |         :ref:`user.user-defined-data-types` in the NumPy manual.\n",
      " |      =  ========================================================================\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> dt = np.dtype('i2')\n",
      " |      >>> dt.isbuiltin\n",
      " |      1\n",
      " |      >>> dt = np.dtype('f8')\n",
      " |      >>> dt.isbuiltin\n",
      " |      1\n",
      " |      >>> dt = np.dtype([('field1', 'f8')])\n",
      " |      >>> dt.isbuiltin\n",
      " |      0\n",
      " |  \n",
      " |  isnative\n",
      " |      Boolean indicating whether the byte order of this dtype is native\n",
      " |      to the platform.\n",
      " |  \n",
      " |  itemsize\n",
      " |      The element size of this data-type object.\n",
      " |      \n",
      " |      For 18 of the 21 types this number is fixed by the data-type.\n",
      " |      For the flexible data-types, this number can be anything.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> arr = np.array([[1, 2], [3, 4]])\n",
      " |      >>> arr.dtype\n",
      " |      dtype('int64')\n",
      " |      >>> arr.itemsize\n",
      " |      8\n",
      " |      \n",
      " |      >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n",
      " |      >>> dt.itemsize\n",
      " |      80\n",
      " |  \n",
      " |  kind\n",
      " |      A character code (one of 'biufcmMOSUV') identifying the general kind of data.\n",
      " |      \n",
      " |      =  ======================\n",
      " |      b  boolean\n",
      " |      i  signed integer\n",
      " |      u  unsigned integer\n",
      " |      f  floating-point\n",
      " |      c  complex floating-point\n",
      " |      m  timedelta\n",
      " |      M  datetime\n",
      " |      O  object\n",
      " |      S  (byte-)string\n",
      " |      U  Unicode\n",
      " |      V  void\n",
      " |      =  ======================\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> dt = np.dtype('i4')\n",
      " |      >>> dt.kind\n",
      " |      'i'\n",
      " |      >>> dt = np.dtype('f8')\n",
      " |      >>> dt.kind\n",
      " |      'f'\n",
      " |      >>> dt = np.dtype([('field1', 'f8')])\n",
      " |      >>> dt.kind\n",
      " |      'V'\n",
      " |  \n",
      " |  metadata\n",
      " |      Either ``None`` or a readonly dictionary of metadata (mappingproxy).\n",
      " |      \n",
      " |      The metadata field can be set using any dictionary at data-type\n",
      " |      creation. NumPy currently has no uniform approach to propagating\n",
      " |      metadata; although some array operations preserve it, there is no\n",
      " |      guarantee that others will.\n",
      " |      \n",
      " |      .. warning::\n",
      " |      \n",
      " |          Although used in certain projects, this feature was long undocumented\n",
      " |          and is not well supported. Some aspects of metadata propagation\n",
      " |          are expected to change in the future.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> dt = np.dtype(float, metadata={\"key\": \"value\"})\n",
      " |      >>> dt.metadata[\"key\"]\n",
      " |      'value'\n",
      " |      >>> arr = np.array([1, 2, 3], dtype=dt)\n",
      " |      >>> arr.dtype.metadata\n",
      " |      mappingproxy({'key': 'value'})\n",
      " |      \n",
      " |      Adding arrays with identical datatypes currently preserves the metadata:\n",
      " |      \n",
      " |      >>> (arr + arr).dtype.metadata\n",
      " |      mappingproxy({'key': 'value'})\n",
      " |      \n",
      " |      But if the arrays have different dtype metadata, the metadata may be \n",
      " |      dropped:\n",
      " |      \n",
      " |      >>> dt2 = np.dtype(float, metadata={\"key2\": \"value2\"})\n",
      " |      >>> arr2 = np.array([3, 2, 1], dtype=dt2)\n",
      " |      >>> (arr + arr2).dtype.metadata is None\n",
      " |      True  # The metadata field is cleared so None is returned\n",
      " |  \n",
      " |  name\n",
      " |      A bit-width name for this data-type.\n",
      " |      \n",
      " |      Un-sized flexible data-type objects do not have this attribute.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> x = np.dtype(float)\n",
      " |      >>> x.name\n",
      " |      'float64'\n",
      " |      >>> x = np.dtype([('a', np.int32, 8), ('b', np.float64, 6)])\n",
      " |      >>> x.name\n",
      " |      'void640'\n",
      " |  \n",
      " |  names\n",
      " |      Ordered list of field names, or ``None`` if there are no fields.\n",
      " |      \n",
      " |      The names are ordered according to increasing byte offset. This can be\n",
      " |      used, for example, to walk through all of the named fields in offset order.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n",
      " |      >>> dt.names\n",
      " |      ('name', 'grades')\n",
      " |  \n",
      " |  ndim\n",
      " |      Number of dimensions of the sub-array if this data type describes a\n",
      " |      sub-array, and ``0`` otherwise.\n",
      " |      \n",
      " |      .. versionadded:: 1.13.0\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> x = np.dtype(float)\n",
      " |      >>> x.ndim\n",
      " |      0\n",
      " |      \n",
      " |      >>> x = np.dtype((float, 8))\n",
      " |      >>> x.ndim\n",
      " |      1\n",
      " |      \n",
      " |      >>> x = np.dtype(('i4', (3, 4)))\n",
      " |      >>> x.ndim\n",
      " |      2\n",
      " |  \n",
      " |  num\n",
      " |      A unique number for each of the 21 different built-in types.\n",
      " |      \n",
      " |      These are roughly ordered from least-to-most precision.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> dt = np.dtype(str)\n",
      " |      >>> dt.num\n",
      " |      19\n",
      " |      \n",
      " |      >>> dt = np.dtype(float)\n",
      " |      >>> dt.num\n",
      " |      12\n",
      " |  \n",
      " |  shape\n",
      " |      Shape tuple of the sub-array if this data type describes a sub-array,\n",
      " |      and ``()`` otherwise.\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      \n",
      " |      >>> dt = np.dtype(('i4', 4))\n",
      " |      >>> dt.shape\n",
      " |      (4,)\n",
      " |      \n",
      " |      >>> dt = np.dtype(('i4', (2, 3)))\n",
      " |      >>> dt.shape\n",
      " |      (2, 3)\n",
      " |  \n",
      " |  str\n",
      " |      The array-protocol typestring of this data-type object.\n",
      " |  \n",
      " |  subdtype\n",
      " |      Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and\n",
      " |      None otherwise.\n",
      " |      \n",
      " |      The *shape* is the fixed shape of the sub-array described by this\n",
      " |      data type, and *item_dtype* the data type of the array.\n",
      " |      \n",
      " |      If a field whose dtype object has this attribute is retrieved,\n",
      " |      then the extra dimensions implied by *shape* are tacked on to\n",
      " |      the end of the retrieved array.\n",
      " |      \n",
      " |      See Also\n",
      " |      --------\n",
      " |      dtype.base\n",
      " |      \n",
      " |      Examples\n",
      " |      --------\n",
      " |      >>> x = numpy.dtype('8f')\n",
      " |      >>> x.subdtype\n",
      " |      (dtype('float32'), (8,))\n",
      " |      \n",
      " |      >>> x =  numpy.dtype('i2')\n",
      " |      >>> x.subdtype\n",
      " |      >>>\n",
      " |  \n",
      " |  type\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(np.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c6b5364",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
