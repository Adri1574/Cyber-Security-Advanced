import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.BFV,      
    poly_modulus_degree=8192,  
    plain_modulus=1032193      
)

context.global_scale = 2**40
context.generate_galois_keys()

encrypted_75 = ts.bfv_vector(context, [75])
encrypted_326 = ts.bfv_vector(context, [326])

encrypted_result = encrypted_75 + encrypted_326

print("\nVersleutelde representatie van de som van 75 en 326:")
print(encrypted_result.serialize())

decrypted_result = encrypted_result.decrypt()

print(f"\nDe ontsleutelde som van 75 en 326 is: {decrypted_result[0]}")