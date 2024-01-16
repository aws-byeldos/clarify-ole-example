- https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html

```
$ curl -X POST -H "Content-Type: application/json" -H "Accept-Type: application/json" -d '[{"features": ["hello"]}, {"features": ["world"]}]' http://localhost:8080/invocations
[{"predictions": "auto-generated-description-for-hello", "probabilities": 0.7123588631337695}, {"predictions": "auto-generated-description-for-world", "probabilities": 0.662554354486929}]%
```