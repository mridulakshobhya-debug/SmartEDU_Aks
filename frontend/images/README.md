# Images Setup Guide

## Slideshow Images

The hero section features an automatic slideshow. To use your images:

### Step 1: Add Your Images
Place your hero section images in the `frontend/images/` folder with these names:
- `hero-1.jpg`
- `hero-2.jpg`
- `hero-3.jpg`
- `hero-4.jpg`

### Step 2: Image Specifications
- **Format**: JPG, PNG, or WebP
- **Dimensions**: 1920x1080px or wider (16:9 aspect ratio recommended)
- **File Size**: Keep under 500KB each for fast loading
- **Quality**: High quality images (compress but don't sacrifice quality)

### Step 3: How It Works
The slideshow in `js/main.js` automatically:
- Displays one image at a time
- Fades between images every 5 seconds
- Shows navigation dots at the bottom
- Supports keyboard navigation (Arrow Left/Right)
- Click dots to jump to specific slides
- Falls back to gradient placeholder if image is missing

### Adding More/Fewer Slides
Edit the `imageList` array in `js/main.js`:

```javascript
const imageList = [
  'images/hero-1.jpg',
  'images/hero-2.jpg',
  'images/hero-3.jpg',
  'images/hero-4.jpg',
  'images/hero-5.jpg'  // Add more images here
];
```

### Example Images
For inspiration, visit: codeacademy.com

You can find professional learning platform imagery there with:
- Students learning
- Technology backgrounds
- Educational themes
- Professional design

### Optimization Tips
1. Use a tool like TinyPNG to compress without losing quality
2. Test images on mobile to ensure they look good
3. Use high contrast backgrounds to ensure text readability
4. Avoid text in images (use overlays instead)
5. Keep consistent color schemes

### Fallback Behavior
If images fail to load, the slideshow will display:
- A solid blue gradient background
- The text "SmartEDU LMS Learning Platform"
- This ensures the page still works without images
