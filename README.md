- https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html
- https://github.com/aws/sagemaker-inference-toolkit
- 
```
$ curl -X POST -H "Content-Type: application/jsonlines" -d '{"features": ["hp desk"]}' http://localhost:8080/invocations

{
  "predictions": "auto-generated-description-for-hp desk",
  "probabilities": 0.21945530682285408
}%
```