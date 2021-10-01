
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle
{
    public:
        int width;
        int height;

        Rectangle()
        {
            width = 0;
            height = 0;
        }

        void display()
        {
            cout << width << " " << height << "\n";
        }
};

class RectangleArea : public Rectangle
{
    public:
        void read_input()
        {
            cin >> width;
            cin >> height;
        }

        void display()
        {
            int area = width * height;
            cout << area << "\n";
        }
};

