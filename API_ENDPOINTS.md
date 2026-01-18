# PetBloom API Endpoints Documentation

## Base URL
- **Development**: `http://localhost:8000/api/v1`
- **Production**: `https://petbloom-frontend-production.up.railway.app/api/v1`

---

## Authentication
All endpoints support optional `Authorization` header for token verification. If not provided, defaults to `temp_user` for development.

```
Authorization: Bearer <firebase_token>
```

---

## Endpoints by Feature

### 1. Users (`/users`)
- `POST /register` - Register new user
- `POST /login` - User login with Firebase token
- `GET /profile` - Get current user profile

### 2. Pets (`/pets`)
- `GET /` - List all available pets for adoption
- `GET /{pet_id}` - Get pet details
- `POST /` - Create new pet (admin)
- `PUT /{pet_id}` - Update pet (admin)

### 3. Products (`/products`)
- `GET /` - List all products
- `GET /{product_id}` - Get product details
- `POST /` - Create new product (admin)
- `PUT /{product_id}` - Update product (admin)

### 4. Cart (`/cart`)
- `GET /` - Get user's shopping cart
- `POST /` - Add item to cart
- `PUT /{item_id}` - Update cart item quantity
- `DELETE /{item_id}` - Remove item from cart

### 5. Wishlist (`/wishlist`)
- `GET /` - Get user's wishlist
- `POST /` - Add pet to wishlist
- `DELETE /{pet_id}` - Remove pet from wishlist

### 6. Orders (`/orders`)
- `GET /` - Get user's order history
- `POST /` - Create new order from cart
- `GET /{order_id}` - Get order details
- `PUT /{order_id}` - Update order status (admin)

### 7. Uploads (`/uploads`)
- `POST /` - Upload image file

### 8. Reviews (`/reviews`) - ✨ NEW
- `GET /product/{product_id}` - Get reviews for a product (includes average rating)
- `GET /pet/{pet_id}` - Get reviews for a pet (includes average rating)
- `GET /{review_id}` - Get specific review
- `POST /` - Create a review (requires either product_id or pet_id)
  ```json
  {
    "productId": "optional_product_id",
    "petId": "optional_pet_id",
    "rating": 1-5,
    "comment": "string"
  }
  ```
- `DELETE /{review_id}` - Delete own review (owner only)

**Response Example:**
```json
{
  "id": "review_123",
  "userId": "user_456",
  "productId": "product_789",
  "rating": 5,
  "comment": "Great quality!",
  "createdAt": "2024-01-18T10:30:00Z"
}
```

### 9. Addresses (`/addresses`) - ✨ NEW
- `GET /` - List all user addresses
- `GET /{address_id}` - Get specific address (owner only)
- `POST /` - Create new address
  ```json
  {
    "street": "123 Main St",
    "city": "Nairobi",
    "state": "Nairobi County",
    "zipCode": "00100",
    "country": "Kenya",
    "isDefault": true
  }
  ```
- `PUT /{address_id}` - Update address (owner only, auto-handles default flag)
- `DELETE /{address_id}` - Delete address (owner only)

**Response Example:**
```json
{
  "id": "address_123",
  "userId": "user_456",
  "street": "123 Main St",
  "city": "Nairobi",
  "state": "Nairobi County",
  "zipCode": "00100",
  "country": "Kenya",
  "isDefault": true,
  "createdAt": "2024-01-18T10:30:00Z"
}
```

### 10. Messages (`/messages`) - ✨ NEW
- `GET /inbox` - Get all messages received (sorted by latest first)
- `GET /conversation/{sender_id}` - Get conversation with specific user (auto-marks as read)
- `GET /{message_id}` - Get specific message (sender/recipient only)
- `POST /` - Send a message
  ```json
  {
    "recipientId": "user_789",
    "content": "Hi, is this pet still available?"
  }
  ```
- `PATCH /{message_id}/read` - Mark message as read (recipient only)

**Response Example:**
```json
{
  "id": "msg_123",
  "senderId": "user_456",
  "recipientId": "user_789",
  "content": "Hi, is this pet still available?",
  "read": false,
  "createdAt": "2024-01-18T10:30:00Z"
}
```

### 11. Seed (`/seed`) - Admin Only
- `POST /init` - Initialize database schema and seed sample data
- `POST /clear` - Clear all data (testing only)
- `POST /init-schema` - Create all database tables

---

## Sample Data Created by Seed

### Pets
- Max (Golden Retriever, 12,000 KSh)
- Whiskers (Persian Cat, 8,000 KSh)
- Buddy (Labrador, 10,000 KSh)

### Products
- Premium Dog Food (5,990 KSh)
- Cat Bed (6,500 KSh)
- Dog Toy Set (3,900 KSh)

### Reviews
- 2 reviews for Premium Dog Food (ratings: 5★, 4★)
- 1 review for Max (5★)

### Addresses
- Default address in Nairobi
- Secondary address in Mombasa

### Messages
- Sample conversation between temp_user and demo_user about Max

---

## Error Responses

### 400 Bad Request
Invalid request parameters or validation error

### 403 Forbidden
User doesn't have permission (e.g., trying to delete another user's review)

### 404 Not Found
Resource not found

### 500 Internal Server Error
Server error

---

## Implementation Details

### Reviews Feature
- Can review either a product OR a pet (not both in same review)
- Prevents duplicate reviews (one review per user per item)
- Automatically calculates average rating and total reviews
- Only owner can delete their review

### Addresses Feature
- Multiple addresses per user supported
- Only one default address at a time
- Setting new default automatically unsets previous default
- User can only view/edit/delete their own addresses

### Messages Feature
- Conversation between two users (sender/recipient)
- Read status tracking
- Getting conversation auto-marks messages as read
- Owner-only deletion and read-marking
- Chronologically sorted by creation date

---

## Testing Examples

### Create a Review
```bash
curl -X POST http://localhost:8000/api/v1/reviews \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_123",
    "rating": 5,
    "comment": "Excellent product!"
  }'
```

### Get Product Reviews
```bash
curl http://localhost:8000/api/v1/reviews/product/product_123
```

### Create an Address
```bash
curl -X POST http://localhost:8000/api/v1/addresses \
  -H "Content-Type: application/json" \
  -d '{
    "street": "456 Oak Ave",
    "city": "Mombasa",
    "state": "Coast County",
    "zipCode": "80100",
    "country": "Kenya",
    "isDefault": true
  }'
```

### Send a Message
```bash
curl -X POST http://localhost:8000/api/v1/messages \
  -H "Content-Type: application/json" \
  -d '{
    "recipientId": "buyer_user_id",
    "content": "Hi, is Max still available for adoption?"
  }'
```

### Get Inbox
```bash
curl http://localhost:8000/api/v1/messages/inbox
```

---

## Database Schema (Prisma)

All new models use automatic ID generation and timestamps:

### Review Model
```prisma
model Review {
  id        String   @id @default(cuid())
  userId    String
  user      User     @relation(fields: [userId], references: [id])
  productId String?
  product   Product? @relation(fields: [productId], references: [id], onDelete: Cascade)
  petId     String?
  pet       Pet?     @relation(fields: [petId], references: [id], onDelete: Cascade)
  rating    Int      // 1-5
  comment   String   @db.Text
  createdAt DateTime @default(now())
}
```

### UserAddress Model
```prisma
model UserAddress {
  id        String   @id @default(cuid())
  userId    String
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  street    String
  city      String
  state     String
  zipCode   String
  country   String
  isDefault Boolean  @default(false)
  createdAt DateTime @default(now())
}
```

### Message Model
```prisma
model Message {
  id          String   @id @default(cuid())
  senderId    String
  sender      User     @relation("MessagesSent", fields: [senderId], references: [id])
  recipientId String
  recipient   User     @relation("MessagesReceived", fields: [recipientId], references: [id])
  content     String   @db.Text
  read        Boolean  @default(false)
  createdAt   DateTime @default(now())
}
```

---

## Next Steps

1. ✅ Backend routes fully implemented
2. ⏳ Frontend integration (create React components for reviews, addresses, messages)
3. ⏳ Deploy to production and test all endpoints
4. ⏳ Add authentication token parsing (currently using temp_user)
5. ⏳ Add admin dashboard for moderation

---

**Last Updated:** January 18, 2024
**Status:** All core backend functionality complete and functional ✅
