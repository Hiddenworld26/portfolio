def spiral_order(matrix):
    """
    Traverse the matrix in spiral order.
    """
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

def unspiral_order(matrix, spiral_order):
    """
    Restore the original matrix from the spiral order.
    """
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * cols for _ in range(rows)]

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    idx = 0
    while top <= bottom and left <= right:
        # Fill top row
        for col in range(left, right + 1):
            result[top][col] = spiral_order[idx]
            idx += 1
        top += 1

        # Fill right column
        for row in range(top, bottom + 1):
            result[row][right] = spiral_order[idx]
            idx += 1
        right -= 1

        # Fill bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result[bottom][col] = spiral_order[idx]
                idx += 1
            bottom -= 1

        # Fill left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result[row][left] = spiral_order[idx]
                idx += 1
            left += 1

    return result

def spiral_shuffle(image):
    """
    Scramble the image pixels in a spiral pattern.
    """
    spiral_order_pixels = spiral_order(image)
    return spiral_order_pixels

def unspiral_shuffle(image, spiral_order_pixels):
    """
    Restore the original image from the spiral-shuffled pixels.
    """
    return unspiral_order(image, spiral_order_pixels)

# Example usage
original_image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

spiral_order_pixels = spiral_shuffle(original_image)
print("Spiral-Shuffled Pixels:", spiral_order_pixels)

restored_image = unspiral_shuffle(original_image, spiral_order_pixels)
print("\nRestored Image:")
for row in restored_image:
    print(row)
