# Prefetch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **int** | Number of seconds prefetch will live for. | [optional] 
**created_at** | **datetime** | Time when prefetch was created. | [optional] 
**computation_time** | **float** | Number of seconds it took to compute results for prefetch. | [optional] 
**result_size_bytes** | **int** | Size of result. | [optional] 
**hit_count** | **int** | Number of times prefetch has been accessed. | [optional] 
**touched_at** | **datetime** | Time when prefetch was last accessed. | [optional] 
**value** | **dict(str, str)** | Data associated with the queries stored by prefetching the data | [optional] 
**url** | **str** | Link to get this item | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


